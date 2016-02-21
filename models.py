import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///data/data.db')

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    slackid = Column(String(100))
    username = Column(String(100))
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=True)
    done = Column(Integer, default=0)

class BrownBag(Base):
    __tablename__ = 'brown_bag'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    selected_date = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))
    done = Column(Integer, default=0)
    user = relationship(User)

class Reminder(Base):
    __tablename__ = 'reminder'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    message = Column(String(255))
    sent = Column(Integer)

def create_tables():
    '''
    create all table in the engine
    '''
    Base.metadata.create_all(engine)

def create_user(**kwargs):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    user = User(**kwargs)
    session.add(user)
    session.commit()
    
    return user
