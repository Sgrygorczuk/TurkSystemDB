import sys
import json

filename1="dummy.json"

# usercredentials: id, username and password
# user: id, type, status, balance
# userinfo: id, pic...

# project: id, devIds.... client
# task: SU 

#load DB from JSON
#DB is the database file
#id is the foreign key
#it return pure dictionary list
def loadDB(DB, id): pass #method not made 
	# == get_row(DB, id)  # in jsonIO.py
			
#push new item to the end of the list
#elements might be array or multiple variables of element
#new user
def push(DB, *args): pass #method not made
	# == add_row(DB, row)

#Given a db, id of user, and the key within the array, modify an existing attribute
def set(DB, id, key, attribute): pass #method not made
	# == set_row(DB, id, key, new_attribute)

#Given a db, id of user, and the key within the array, get a certain attribute
def get(DB, id, key): pass #method not made
	# == get_value(DB, id, key)

#Given a db and the key within the array, find a certain attribute from top down
#unless it is reversed
def find(DB, key, attribute, reversed = False): pass #method not made

#remove a whole row
def remove(DB, id):
	# == del_row(DB, id)

#get last id of a DB
def getlastId(DB): pass #method not made
	# == get_last_id(DB)