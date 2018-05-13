from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, extract
from sqlalchemy.orm import sessionmaker
from models import *
from functions import *
import datetime

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

def show_entry_menu():
	choice = show_entry_menu_choice()
	if choice == 't':
		show_today_entries()

	if choice == 'm':
		show_month_entries()

	if choice == 'b':
		display_menu()

	if choice == 'd':
		date = input("Date(dd) : ")
		month = input("Month(mm) : ")
		year = input("Year(yyyy) : ")
		d = datetime.datetime.strptime(date+month+year,"%d%m%Y").date()
		show_another_day_entries(d)
	
	if choice == 'a':
		month = input("Month(mm) : ")
		year = input("Year(yyyy) : ")
		show_another_month_entries(month, year)

	if choice == 'q':
		display_menu()
		print("Come back\n")
		exit()

def show_today_entries():
	display_menu()
	now = datetime.date.today()
	print("TODAY'S ENTRIES\n")
	#entries = session.query(Entry).filter(extract('year',Entry.create_date)==now.year, extract('month',Entry.create_date)==now.month,extract('day',Entry.create_date)==now.day)
	entries = session.query(Entry).filter(Entry.create_date == now)
	num = 1
	for entry in entries :
		print(str(num)+". "+entry.title)
		print("(on "+str(entry.create_date)+" )\n")
		print(entry.content+"\n")
		print("\n")
		num = num + 1
		
	print("\n\n\n")
	choice = show_today_entries_choice()
	if choice == 'a':
		create_entry()

	if choice == 'd':
		entry_num = input("Entry number : ")
		delete_entry(entries[int(entry_num)-1].id, 1)

	if choice == 'b':
		show_entry_menu()

	if choice == 'h':
		display_menu()
		arr = []

	if choice == 'q':
		display_menu()
		print("It's okay.\n")
		exit()


def show_another_day_entries(day):
	display_menu()
	print("ENTRIES OF " + str(day))
	entries = session.query(Entry).filter(Entry.create_date == day).all()
	num = 1
	for entry in entries :
		print(str(num)+". "+entry.title)
		print("(on "+str(entry.create_date)+" )\n")
		print(entry.content+"\n")
		print("\n")
		num = num + 1
		
	choice = show_month_entries_choice()
	if choice == 'd':
		entry_num = input("Entry number : ")
		delete_entry(entries[int(entry_num)-1].id, 3)

	if choice == 'b':
		show_entry_menu()

	if choice == 'h':
		display_menu()
		arr = []

	if choice == 'q':
		display_menu()
		print("It's okay.\n")
		exit()


def show_month_entries():
	display_menu()
	now = datetime.date.today()
	print("THIS MONTH'S ENTRIS\n")
	#entries = session.query(Entry).filter(extract('year',Entry.create_date)==now.year, extract('month',Entry.create_date)==now.month,extract('day',Entry.create_date)==now.day)
	entries = session.query(Entry).filter(extract('month',Entry.create_date) == now.month)
	num = 1
	for entry in entries :
		print(str(num)+". "+entry.title)
		print("(on "+str(entry.create_date)+" )\n")
		print(entry.content+"\n")
		print("\n")
		num = num + 1
		
	choice = show_month_entries_choice()
	if choice == 'd':
		entry_num = input("Entry number : ")
		delete_entry(entries[int(entry_num)-1].id, 2)

	if choice == 'b':
		show_entry_menu()

	if choice == 'h':
		display_menu()
		arr = []

	if choice == 'q':
		display_menu()
		print("It's okay.\n")
		exit()


def show_another_month_entries(month, year):
	display_menu()
	print("ENTRIES OF "+month+"/"+year+" : \n")
	entries = session.query(Entry).filter(extract('year',Entry.create_date)==year, extract('month',Entry.create_date)==month).all()
	num = 1
	for entry in entries :
		print(str(num)+". "+entry.title)
		print("(on "+str(entry.create_date)+" )\n")
		print(entry.content+"\n")
		print("\n")
		num = num + 1
		
	choice = show_month_entries_choice()
	if choice == 'd':
		entry_num = input("Entry number : ")
		delete_entry(entries[int(entry_num)-1].id, 2)

	if choice == 'b':
		show_entry_menu()

	if choice == 'h':
		display_menu()
		arr = []

	if choice == 'q':
		display_menu()
		print("It's okay.\n")
		exit()
	

def create_entry():
	display_menu()
	title = input("Title : ")
	content = input("Entry : ")
	new_entry=Entry(title = title, content = content)
	session.add(new_entry)
	session.commit()
	print("Entry created \n")
	print("[h] Go to home\n")
	print("[t] See today's entries\n")
	print("[q] Quit\n")
	choice = input("")
	if choice == 'h':
		display_menu()

	if choice == 't':
		show_today_entries()

	if choice == 'q':
		print(":)\n")
		exit()


def delete_entry(entry_id , f):
	entry = session.query(Entry).filter(Entry.id == entry_id).first()
	session.delete(entry)
	session.commit()
	if f==1:
		show_today_entries()

	elif f==2:
		show_month_entries()

	elif f==3:
		show_another_day_entries(entry.create_date)
