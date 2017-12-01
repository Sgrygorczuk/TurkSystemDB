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
#ex: get_value(User(), "name", 0)
#	 returns: System Admit
def get_value(obj, key, id = 'Nan'):
    if id == 'Nan':
        id = obj.get_id()
        if not key:
            print("Key not stated")
            return None
        elif id == 'Nan':
            print("ID not initialized")
            return None
        else:
            #can pull from user
            method = 'get_'+key
            try:
                value = getattr(obj, method)()
                return value
            except:
                print("No such key exist")
                return None
    #otherwise just search db
    value = jsonIO.get_value(obj.db, id, key)
    if value == None:
        print("Either the id or key does not exist")
    return value
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
#post: returns the whole column of an attribute
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
#####***************************might break at bid_log call*************	
#pre: any DB array	
#post: print table
def print_table(m):
	if not m:
		return 0
	if type(m) == list:
		keys = list(m[0].keys())
	else:
		keys = list(m.keys())
	values = []
	indents = "{:<15}"
	for i in range(0, len(keys)-1):
		indents += " {:<15}"
	print (indents.format(*keys))
	#is it a list of dictionary?
	if type(m) == list:
		for item in m:
			values = item.values()
			values = list(values)
			val_print(values)
	else: #it's a dictionary
		val_print(list(m.values()))
	return 1
#to be called by print_table
#values hold collection of values
def val_print(values):
    for j in range(len(values)):
        value = values[j]
        #is the value a list?
        if type(value) == list:
            if value == []:
                values[j] = '[]'
            else:
                values[j] =  ",".join(str(x) for x in value)
    print (indents.format(*values))
	
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
#cond: dev    avg (dev,"team")
#      team   avg (team,"team")
#      client avg (client, "client")
#pre: id must exists for all 
#post: return average
def calc_avg_rating(obj,user):
	ratings = []
	user+="_rating"
	for id in obj.get_project_ids():
		ratings.append(jsonIO.get_value(obj.db, id, "team_rating"))
	#if ratings exist return something
	if ratings:
		return max(numpy.mean(ratings), 1)
	return None