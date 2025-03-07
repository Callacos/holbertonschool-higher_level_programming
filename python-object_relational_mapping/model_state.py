#!/usr/bin/python3
"""
This is the end, hold your breath and count to ten
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """
    This is the State class"""
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
