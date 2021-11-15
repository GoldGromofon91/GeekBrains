import inspect

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .CONFIGS import CONFIG_PROJECT


class SingletonDBMeta(type):
    pass


class Singleton(metaclass=SingletonDBMeta):
    pass


class ServerDB(Singleton):
    def __init__(self, base, db_name=None):
        self.db_name = CONFIG_PROJECT['DEFAULT_CONF']['DB_NAME_ENGINE'] + db_name if db_name \
            else CONFIG_PROJECT['DEFAULT_CONF']['DB_NAME_ENGINE'] + CONFIG_PROJECT['DEFAULT_CONF']['DB_NAME']

        self.engine = create_engine(self.db_name)
        self.base = base
        self.session = None

    def open_connect(self):
        self.base.metadata.create_all(bind=self.engine)
        s_maker = sessionmaker(self.engine)
        self.session = s_maker()

    def close_connect(self):
        if self.session:
            self.session.close()
            self.session = None


class SessionContext:
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
            inspect_stack = inspect.stack()[1][3]
            raise Exception(f'Error in {inspect_stack}')
