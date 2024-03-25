from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    workouts = relationship("Workout", back_populates="owner")
    goals = relationship("Goal", back_populates="owner")

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String, index=True)
    duration = Column(Integer)
    date = Column(DateTime)
    notes = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="workouts")

class Goal(Base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True, index=True)
    goal_type = Column(String, index=True)
    target = Column(Integer)
    deadline = Column(DateTime)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="goals")
