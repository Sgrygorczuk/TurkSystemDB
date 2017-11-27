import sys
import json

filename1="dummy.json"

usercredentials: id, username and password
user: id, type, status, balance
userinfo: id, pic...

project: id, devIds.... client
task: SU 

#load DB from JSON
#DB is the database file
#id is the foreign key
#it return pure dictionary list
def loadDB(DB, id): pass #method not made
	# data = []
	# file = findDB(DB)
	# cont = false
	# with open(file) as f:
		# for line in f:
			# if "id" in data.append(jason.loads(line)) == id or cont:
				# if "id" and cont!=0:
					# cont = true
			# return data
			
#push new item to the end of the list
#elements might be array or multiple variables of element
#new user
def push(DB, *args): pass #method not made
	#first must break down args and transform it into dictionary form
	# with open (file_out,'w+') as txt:
		# json.dump(data, jsonFile)

#modify an existing attribute
def set(DB, id, key, attribute):
	pass #method not made
	
#find a certain attribute
def find(DB, id, attribute):
	pass #method not made

#remove a whole row
def remove(DB, id):
	pass #method not made

#get last id of a DB
def getlastId(DB):
	pass #method not made