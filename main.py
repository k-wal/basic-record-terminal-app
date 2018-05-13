import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from datetime import datetime
from functions import *
import entry


#Base = declarative_base()

engine = create_engine('sqlite:///database.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
Base.metadata.create_all(engine)
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


display_menu()
choice = ''
while choice != 'q':
    
    choice = display_initial_choice()
    display_menu()

    if choice == '1':
        print("functionality currently unavaialable\n")
        entry.show_entry_menu()

    elif choice == '2':
        print("functionality currently unavaialable\n")
        entry.create_entry()

    elif choice == 'q': 
        print("Have a nice day, yeah?\n")

    else :
        print("choice not recognized")

