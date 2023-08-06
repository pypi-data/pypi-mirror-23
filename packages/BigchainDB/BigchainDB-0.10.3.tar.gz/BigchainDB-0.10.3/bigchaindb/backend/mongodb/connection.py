import time
import logging

import pymongo

import bigchaindb
from bigchaindb.utils import Lazy
from bigchaindb.common.exceptions import ConfigurationError
from bigchaindb.backend.exceptions import (DuplicateKeyError,
                                           OperationError,
                                           ConnectionError)
from bigchaindb.backend.connection import Connection

logger = logging.getLogger(__name__)


class MongoDBConnection(Connection):

    def __init__(self, replicaset=None, ssl=None, login=None, password=None, **kwargs):
        """Create a new Connection instance.

        Args:
            replicaset (str, optional): the name of the replica set to
                                        connect to.
            **kwargs: arbitrary keyword arguments provided by the
                configuration's ``database`` settings
        """

        super().__init__(**kwargs)
        self.replicaset = replicaset or bigchaindb.config['database']['replicaset']
        self.ssl = ssl if ssl is not None else bigchaindb.config['database'].get('ssl', False)
        self.login = login or bigchaindb.config['database'].get('login')
        self.password = password or bigchaindb.config['database'].get('password')

    @property
    def db(self):
        return self.conn[self.dbname]

    def query(self):
        return Lazy()

    def collection(self, name):
        """Return a lazy object that can be used to compose a query.

        Args:
            name (str): the name of the collection to query.
        """
        return self.query()[self.dbname][name]

    def run(self, query):
        try:
            try:
                return query.run(self.conn)
            except pymongo.errors.AutoReconnect as exc:
                logger.warning('Lost connection to the database, '
                               'retrying query.')
                return query.run(self.conn)
        except pymongo.errors.AutoReconnect as exc:
            raise ConnectionError from exc
        except pymongo.errors.DuplicateKeyError as exc:
            raise DuplicateKeyError from exc
        except pymongo.errors.OperationFailure as exc:
            raise OperationError from exc

    def _connect(self):
        """Try to connect to the database.

        Raises:
            :exc:`~ConnectionError`: If the connection to the database
                fails.
        """

        try:
            # we should only return a connection if the replica set is
            # initialized. initialize_replica_set will check if the
            # replica set is initialized else it will initialize it.
            initialize_replica_set(self.host, self.port, self.connection_timeout,
                                   self.dbname, self.ssl, self.login, self.password)

            # FYI: this might raise a `ServerSelectionTimeoutError`,
            # that is a subclass of `ConnectionFailure`.
            client = pymongo.MongoClient(self.host,
                                         self.port,
                                         replicaset=self.replicaset,
                                         serverselectiontimeoutms=self.connection_timeout,
                                         ssl=self.ssl)

            if self.login is not None and self.password is not None:
                client[self.dbname].authenticate(self.login, self.password)

            return client

        # `initialize_replica_set` might raise `ConnectionFailure` or `OperationFailure`.
        except (pymongo.errors.ConnectionFailure,
                pymongo.errors.OperationFailure) as exc:
            raise ConnectionError() from exc


def initialize_replica_set(host, port, connection_timeout, dbname, ssl, login, password):
    """Initialize a replica set. If already initialized skip."""

    # Setup a MongoDB connection
    # The reason we do this instead of `backend.connect` is that
    # `backend.connect` will connect you to a replica set but this fails if
    # you try to connect to a replica set that is not yet initialized
    conn = pymongo.MongoClient(host=host,
                               port=port,
                               serverselectiontimeoutms=connection_timeout,
                               ssl=ssl)

    if login is not None and password is not None:
        conn[dbname].authenticate(login, password)

    _check_replica_set(conn)
    host = '{}:{}'.format(bigchaindb.config['database']['host'],
                          bigchaindb.config['database']['port'])
    config = {'_id': bigchaindb.config['database']['replicaset'],
              'members': [{'_id': 0, 'host': host}]}

    try:
        conn.admin.command('replSetInitiate', config)
    except pymongo.errors.OperationFailure as exc_info:
        if exc_info.details['codeName'] == 'AlreadyInitialized':
            return
        raise
    else:
        _wait_for_replica_set_initialization(conn)
        logger.info('Initialized replica set')


def _check_replica_set(conn):
    """Checks if the replSet option was enabled either through the command
       line option or config file and if it matches the one provided by
       bigchaindb configuration.

       Note:
           The setting we are looking for will have a different name depending
           if it was set by the config file (`replSetName`) or by command
           line arguments (`replSet`).

        Raise:
            :exc:`~ConfigurationError`: If mongod was not started with the
            replSet option.
    """
    options = conn.admin.command('getCmdLineOpts')
    try:
        repl_opts = options['parsed']['replication']
        repl_set_name = repl_opts.get('replSetName', repl_opts.get('replSet'))
    except KeyError:
        raise ConfigurationError('mongod was not started with'
                                 ' the replSet option.')

    bdb_repl_set_name = bigchaindb.config['database']['replicaset']
    if repl_set_name != bdb_repl_set_name:
        raise ConfigurationError('The replicaset configuration of '
                                 'bigchaindb (`{}`) needs to match '
                                 'the replica set name from MongoDB'
                                 ' (`{}`)'.format(bdb_repl_set_name,
                                                  repl_set_name))


def _wait_for_replica_set_initialization(conn):
    """Wait for a replica set to finish initialization.

    If a replica set is being initialized for the first time it takes some
    time. Nodes need to discover each other and an election needs to take
    place. During this time the database is not writable so we need to wait
    before continuing with the rest of the initialization
    """

    # I did not find a better way to do this for now.
    # To check if the database is ready we will poll the mongodb logs until
    # we find the line that says the database is ready
    logger.info('Waiting for mongodb replica set initialization')
    while True:
        logs = conn.admin.command('getLog', 'rs')['log']
        if any('database writes are now permitted' in line for line in logs):
            return
        time.sleep(0.1)
