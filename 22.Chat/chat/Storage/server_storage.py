from sqlalchemy import Column, Integer, String, create_engine, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    info = Column(String,nullable=True)

    def __init__(self, login, info=None):
        self.login = login
        self.info = info


    def __repr__(self):
        return f'<{self.__class__.__name__}>({self.login})'


class ClientHistory(Base):
    __tablename__ = 'user_history'

    id = Column(Integer, primary_key=True)
    datetime_at = Column(DateTime)
    ip = Column(String, nullable=True)

    def __init__(self, datetime_at, ip):
        self.datetime_at = datetime_at
        self.ip = ip

    def __repr__(self):
        return f'<{self.__class__.__name__}>({self.login})'


class ContactsList(Base):
    __tablename__ = 'contacts_list'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer)
    client_id = Column(Integer, ForeignKey('client.id'))

    def __init__(self, datetime_at, ip):
        self.datetime_at = datetime_at
        self.ip = ip

    def __repr__(self):
        return f'<{self.__class__.__name__}>({self.login})'

engine = create_engine('sqlite:///server.sqlite', echo=False)
Base.metadata.create_all(engine)
