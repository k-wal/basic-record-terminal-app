import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
 
Base = declarative_base()
 
class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True, autoincrement = True)
    title = Column(String(50))
    content = Column(String(250), nullable = False)
    create_date = Column(Date, default = datetime.date.today())
    
    def serialize(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'content' : self.content,
            'create_date' : self.create_date
        }

    def __repr__(self):
        return self.serialize().__repr__()
