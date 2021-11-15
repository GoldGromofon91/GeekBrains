import datetime

from sqlalchemy import Column, Integer, String, create_engine, DateTime, ForeignKey, Table, Text
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

from .db_conf import SessionContext

Base = declarative_base()


class Core:
    __tablename__ = 'core'

    created_at = Column(DateTime, default=datetime.datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow(),
                        nullable=False)

    @classmethod
    def get_all(cls, session):
        with SessionContext(session) as session:
            return session.query(cls).all()

    @classmethod
    def into(cls, session, *args, **kwargs):
        with SessionContext(session) as session:
            obj = cls(*args, **kwargs)
            session.add(obj)

    @classmethod
    def get_by_id(cls, session, id):
        obj = session.query(cls).filter(cls.id == id).first()
        return obj

    def update(self, session, *args, **kwargs):
        with SessionContext(session) as session:
            for key, val in kwargs.items():
                setattr(self, key, val)
                session.add(self)
                session.commit()

    def drop(self, session):
        with SessionContext(session) as session:
            session.delete(self)
            session.commit()


user_to_chat_table = Table('user_to_chat',
                           Base.metadata,
                           Column('user_id', Integer, ForeignKey('user.id')),
                           Column('chat_id', Integer, ForeignKey('chat.id')))


class User(Core, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String(32), unique=True, nullable=False)
    first_name = Column(String(64), nullable=True)
    info = Column(String(128), nullable=True)
    password = Column(String(128))

    chat = relationship('Chat', secondary=user_to_chat_table, backref='user')
    message = relationship('UserMessage', backref='owner')
    history = relationship('UserHistory', backref='owner')

    def __init__(self, client):
        self.login = client.get('login')
        self.password = client.get('password')
        self.first_name = client.get('first_name')
        self.info = client.get('info')

    def __repr__(self):
        return f'<{self.__class__.__name__}>({self.login})'

    @classmethod
    def get_user_by_login(cls, session, login):
        obj = session.query(cls).filter(cls.login == login).first()
        return obj


class Chat(Core, Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)

    message = relationship('UserMessage', backref='owner')

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f'<{self.__class__.__name__}>({self.title})'


class ContactsList(Base):
    __tablename__ = 'contacts_list'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    contact_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, owner_id, contact_id):
        self.owner_id = owner_id
        self.contact_id = contact_id

    def __repr__(self):
        return f'<{self.__class__.__name__}>)'

    @classmethod
    def get_all_contacts(cls, session, owner_id):
        obj = session.query(cls).filter_by(cls.owner_id == owner_id).all()


class UserHistory(Core, Base):
    __tablename__ = 'user_history'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    ip = Column(String(64), nullable=True)

    def __init__(self, owner_id, ip_addr):
        self.owner_id = owner_id
        self.ip = ip_addr

    def __repr__(self):
        return f'<{self.__class__.__name__}>)'


class UserMessage(Core, Base):
    __tablename__ = 'user_message'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    chat_id = Column(Integer, ForeignKey('chat.id'))
    text = Column(Text)

    def __init__(self, owner_id, chat_id, text):
        self.owner_id = owner_id
        self.chat_id = chat_id
        self.text = text

    def __repr__(self):
        return f'<{self.__class__.__name__}>)'
