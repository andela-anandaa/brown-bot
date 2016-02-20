from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=True)
    done = Column(Integer)

class BrownBag(Base):
    __tablename__ = 'brown_bag'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    selected_date = Column(Date)
    user = relationship(User)

class Reminder(Base):
    __tablename__ = 'reminder'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    message = Column(String(255))
    sent = Column(Integer)

class MessageLog(Base):
    __tablename__ = 'message_log'
    id = Column(Integer, primary_key=True)
    type = Column(String(20)) # incoming or outgoing
    message = Column(String(255))
    user = relationship(User)

engine = create_engine('sqlite:///data/data.db')

def migrations():
    '''
    create all table in the engine
    '''
    Base.metadata.create_all(engine)
