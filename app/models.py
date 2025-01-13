from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    parent_id = Column(Integer, ForeignKey('activities.id'), nullable=True)

    parent = relationship("Activity", remote_side=[id], backref="children")

class Building(Base):
    __tablename__ = 'buildings'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)

class Organization(Base):
    __tablename__ = 'organizations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String)
    building_id = Column(Integer, ForeignKey('buildings.id'))
    activity_id = Column(Integer, ForeignKey('activities.id'))

    building = relationship('Building', back_populates="organizations")
    activity = relationship('Activity', back_populates="organizations")

Building.organizations = relationship('Organization', back_populates="building")
Activity.organizations = relationship('Organization', back_populates="activity")
