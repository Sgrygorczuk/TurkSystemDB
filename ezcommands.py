from User import *
from Project import *
from Team import *
from Bid import *
from Task import *
from jsonIO import *
import inspect
import numpy

##########################################################################
##########################################################################
########						NOTES:							  ########
####																  ####
####	Use this functions to ensure that the creation of your 		  ####
####  classes does not conflict with other classes, all the other     ####
####	classes are updated if they share the same key.			      ####
####																  ####
####	This will also makes sure that there no duplicates and 		  ####
####     blacklisted user/project/bid... so forth are created.	      ####
####																  ####
####		Finally this class will aid in other calculations.		  ####
########														  ########
##########################################################################
##########################################################################


###DIRECT DATABASE ACCESS######DIRECT DATABASE ACCESS######DIRECT DATABASE ACCESS###

#pre: given an instance of a class, key, and id (unless id is initialized in object)
#post: get attribute from a class 
#	   else return None
#ex: get_item(User(), "name", 0)
#	 returns: System Admit
#**************************************************not working with just obj & key
def get_item(obj, key, id = 'Nan'):
	if id == 'Nan':
		id = obj.get_id()
		if not key:
			print("Key not stated")
			return None
		if id == 'Nan':
			print("ID not initialized")
			return None
		else:
			#can pull from user
			method = 'get_'+key+'()'
			method = getattr(obj, method)
			print(method)
			return obj.method
	#otherwise just search db
	print(1)
	return jsonIO.get_value(obj.db, id, key)
	
#post: returns all items in a database
def get_all_db(obj):
	return jsonIO.read_rows(obj.db)

#pre: id must exist	(must include id unless id is initialized in object)
#post: returns all attribute of class
#      else return None
def get_row(obj, id = 'Nan'):
	if id == 'Nan':
		id = obj.get_id()
		if id == 'Nan':
			print("ID not initialized")
			return None
		else:
			#can pull from user
			return obj.get_all()
	elif isinstance(id, str):
		print("ID does not exits")
		return None
	#otherwise just search db
	return jsonIO.get_row(obj.db, id)
	
#pre: needs valid instance of class and its key
#pro: returns the whole column of an attribute
#******************************************************not tested from here down
def get_col(obj, key):
	array = []
	#don't include SU (id = 0)
	n = 0
	if obj.__class__ == User:
		n += 1
	for id in range(n, jsonIO.get_last_id(obj.db)):
		attrib = jsonIO.get_value(obj.db, id, key)
		#if it exist
		if attrib!= None:
			array.append({"id": id, key: attrib})
	return array
	
#***************************************might not be correct****************************
#pre: any DB array	
#post: print table
def print_table(m):
	if not m:
		return 0
	keys = []
	values = []
	indents = "{:<20}"
	for key, value in my_dict.iteritems():
		keys.append(key)
		values.append(value)
	for i in range(0, len(keys)-1):
		indents += "{ :<20}"
	print (indents.format(keys))
	for value in values:
		print (indents.format(value))
	return 1

	
###SU######SU######SU######SU######SU######SU######SU######SU######SU######SU######SU###

#pre: needs a valid user of type user and could also do it from an id
#post: returns dictionary of status of the user: user_type, status, warning, and balance
#else returns None
def user_report(user, id = 'Nan'):
	if user.__class__ != User:
		print("User is not of type User")
		return None
	if id == 'Nan':
		id = user.get_id()
		if id == 'Nan':
			print("ID not initialized")
			return None
		else:
			#can pull from user
			return {"user_type":user.get_user_type(), "status":user.get_status(),
			"warning":user.get_warning(), "balance":user.get_balance()}
	obj = jsonIO.get_row(user.db, id)
	if obj == None:
		return None
	return {"user_type":obj["user_type"], "status":obj["status"],
	"warning":obj["warning"], "balance":obj["balance"]}

#authenticate user
#cond: will autheticate user: username or username and password for logging in
#pre: user must have id, username, and password
#post: will return string of "success" or failure message
def autheticate(username, password = ""):
	pass

###CLASS CREATION######CLASS CREATION######CLASS CREATION######CLASS CREATION###

#pre: takes required attribute of new user
#post: places temp_user in SU tasks
def register_user():
	pass


#will take what is required for 
def start_project():
	pass

#must have client and project id for input
#takes required feature for a bid and initiates a bid
def start_bid():
	pass	

	#from,to,amount
def tranfer_funcs(from_user, to_user, amount):
	pass

	
###METRICS######METRICS######METRICS######METRICS######METRICS######METRICS###
#pre: get Team() object or User() where devs exit with their ids
#post: return average
def calc_avg_rating(object):
	ratings = []
	if object.__class__ == Team:
		for id in object.get_dev_ids():
			ratings.append(get_attribute(object, id, "ratings"))
		(numpy.asarray(ratings)).flatten()
	else:
		ratings = object.get_ratings()
	return max(numpy.mean(ratings), 1)