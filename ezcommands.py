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

###########################DIRECTORY OF FUNCTIONS#########################
#Direct Databse access
#get_value(obj, key, id = 'Nan'): gets value
#get_all_db(obj): gets all from db
#get_row(obj, key): gets an entire row
#print_table(m): prints the table given a dictionary or a list of it
#----------------------------------------------------------------------------
#SU
#user_report(user, id = 'Nan'): returns status of the user:
#                               user_type, status, warning, and balance
#verify(username, password = ""): returns [case number, user, message]
#----------------------------------------------------------------------------
#Class creation
#user_exists(username): returns 1 if user exist else returns 0
#register_user(name, username, password, user_type, deposit):
#              places new temp_user in SU tasks
#create_project(): will return and make a new project
#create_bid(project_id, start_date, end_date, initial_bid): returns a new bid
#
#---------------------------------------------------------------------------
#Special functions
#project_fund_transfer(from_user, to_user, amount): it will modify both 
#             balances and create task. Check below for more details.
#----------------------------------------------------------------------------
#Metrics
#calc_avg_rating(obj,user): returns the average rating of dev, team, or client
#----------------------------------------------------------------------------
#Helper functions
#find_row(db, key, value): returns row of given key value
#val_print(values): support method for print_table method
#get_time(): returns current date time in Y-m-d H:M:S form
#string_to_datetime(time): returns datetime form
#datetime_to_string(dt_time): returns string form
#get_n_days_later(time, n): return string with added days 
#tranfer_funds(from_user, to_user, amount): it will modify both balances
#############################################################################

#/\/\/\/\DIRECT DATABASE ACCESS/\/\/\/\DIRECT DATABASE ACCESS/\/\/\/\DIRECT DATABASE ACCESS/\/\/\/\

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
			#from helper function (can be found all the way below)
			val_print(values)
	else: #it's a dictionary
		val_print(list(m.values()))
	return 1
	
	
#/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\

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
# and return [case number, user, message]
#pre: none
#post: will return [case number, user, message] along with a print
def verify(username, password = None):
    case = 1
    user = {}
    message = ""
    #empty inputs
    if not username:
        message = "Username field is empty"
    elif password == "":
        case = 2
        message = "Password field is empty"
    else:
        #check without password
		#find_row is a helper function (can be found all the way below)
        user = find_row("user_db", "username", username)
        if not user:
            case = 3
            message = "Username not found"
        elif user["status"] == "blacklisted":
            case = 4
            message = "User found but blacklisted"
        elif password == None:
            if user["warning"] == 2:
                if user["status"] != "blacklisted":
                    case = 5
                    message = "User found, but has 2 warnings and not yet black listed"
                #blacklisted already checked
            elif user["status"] == "rejected":
                case = 6
                message = "Temporary user was rejected and password not yet verified"
            else:
                case = 7
                message = "User has no warnings and password not yet verified"
        #check with password
        elif user["password"] != password:
            case = 8
            message = "Your password does not match"
        elif user["warning"] == 2:
            if user["status"] != "blacklisted":
                case = 9
                message = "Login successful, but has 2 warnings and not yet black listed"
        elif user["status"] == "rejected":
                case = 10
                message = "Login successful, but temporary user was rejected"
        else: #user["password"] matches
            case = 0
            message = "Login successful"
    print(message)
    return [case, user, message]
	
#/\/\/\/\CLASS CREATION/\/\/\/\CLASS CREATION/\/\/\/\CLASS CREATION/\/\/\/\

#pre: none
#post: returns 1 if user exist else returns 0
def user_exists(username):
    return 1 if find_row("user_db", "username", username) else 0

#pre: takes required attribute of new user, username should not exist
#post: places new temp_user in SU tasks
def register_user(name, username, password, user_type, deposit):
    #empty inputs
    if username == "":
        print("Username field is empty")
        return None
    elif user_exists(username):
        print("That username already exists")
        return None
    elif password == "":
        print("Password field is empty")
        return None
    elif name == "":
        print("Name field is empty")
        return None
    #check values
    elif len(password) > 64:
        print("That password is too long")
        return None
    elif len(name) > 80:
        print("That name is too long")
        return None
    elif not name.isalpha():
        print("That name has numbers or special charaters")
        return None
    elif user_type != "client" and user_type != "dev" and user_type!= "SU":
        print("That is not a valid user type")
        return None
    #see if deposit is a positive integer
    else:
        try:
            val = float(deposit)
            #check deposit syntax
            val = str(deposit)
            if '.' in val:
                if len(val.rsplit('.')[-1]) > 2:
                    print("That is not a valid deposit")
                    return None
            #check deposit amount
            if deposit <= 0:
                print("The deposit is too low")
                return None
			#create User and Task
            print ("User made")
            user = User(name, username, password, user_type, "temp", deposit)
            return [user,
                    Task(user.get_id(),"new user")]
		#this was when deposit was not right syntax
        except ValueError:
            print("That is not a valid deposit")
            return None

#pre: needs all the entries filled and an existing client id
#post: will return and make a new project
def create_project(client_id, title, desc, start_date, end_date):
    #check empty
    if title == "":
        print("Title field is empty")
        return None
    if desc == "":
        print("Description field is empty")
        return None
    if start_date == "":
        print("Start date field is empty")
        return None
    if end_date == "":
        print("End date field is empty")
        return None
    if not find_row("user_db","id", client_id):
        print("User not found")
        return None
	#make sure end time > start time
    #uses helper_function
    s_date = string_to_datetime(start_date)
    e_date = string_to_datetime(end_date)
    if s_date >= e_date:
        print("The end date must be after the start date")
        return None
    return Project(client_id, title, desc, start_date, end_date)

#pre: must have client and project id for input and bid_id must be new
#    end>start date and client's balance >= bid
#post: returns a new bid
def create_bid(project_id, start_date, end_date, initial_bid):
    #check empty
    if start_date == "":
        print("Start date field is empty")
        return None
    if end_date == "":
        print("End date field is empty")
        return None
    #check amount is positive
    if initial_bid < 0:
        print("Initial bid must be positive")
        return None
    #check id consistencies
    project = jsonIO.get_row("project_db", project_id)
    if not project:
        print("Project not found")
        return None
    bid = jsonIO.get_row("bid_db", project_id)
    if bid:
        print("Bid already exists")
        return None
    user = jsonIO.get_row("user_db", project["client_id"])
    if not user:
        print("User not found")
        return None
    #make sure client has money
    if float(user["balance"]) < initial_bid:
        print("User does not have enough funds")
        return None
    #make sure end time > start time
	#uses helper_function
    s_date = string_to_datetime(start_date)
    e_date = string_to_datetime(end_date)
    if s_date >= e_date:
        print("The end date must be after the start date")
        return None
    return Bid(project_id, start_date, end_date, initial_bid)
	
	
#/\/\/\/\SPECIAL FUNCTIONS/\/\/\/\SPECIAL FUNCTIONS/\/\/\/\SPECIAL FUNCTIONS/\/\/\/\ 

#cond: this is called at the beginning after the bid is done
#      the SU will withdraw the money and take 10% then give
#      half of the money to the team, and will add to SU task.
#      It will be set as resolved, and set as unresolved when
#      the team submits their work or until the deadline.
#pre: from, to users exist and amount exists and is valid
#post: it will modify both balances and create task.
def project_fund_transfer(from_user, to_user, amount):
	if amount <= 0:
		print("Must have a positive amount")
		return 0
	if from_user.get_id() == 'Nan':
		print("The user you are grabbing from does not exist")
		return 0
	if to_user.get_id() == 'Nan':
		print("The user you are sending to does not exist")
		return 0
	if from_user.get_balance() < amount:
		print("The user does not have enough funds")
		return 0
	if not from_user.get_project_ids:
		print("The client has not initiated a project")
		return 0
	from_user.withdraw(amount)
	#take 10% and take 50% until completion of project
	deduction = round(amount*.1*.5, 2)
	amount -= deduction
	#keep it in superuser's bank
	jsonIO.set_value("user_db", 0, "balance", deduction)
	to_user.deposit(amount)
	#create a new task to retrieve the other 40% = 50%-10# fee
	Task(from_user.get_project_ids[-1], "new project", True)
	
	
#/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\

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
	
#/\/\/\/\HELPER FUNTIONS/\/\/\/\HELPER FUNTIONS/\/\/\/\HELPER FUNTIONS/\/\/\/\
#pre: must have a valid db, key and value
#post: returns row of given key value
def find_row(db, key, value):
	rows = jsonIO.get_rows(db, key, value)
	if rows:
		return rows[0]
	else:
		return {}

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

#post: return time now in string
def get_time():
	return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	
#pre: needs String in Y-m-d H:M:S form
#post: returns datetime form
def string_to_datetime(time):
	try:
		return datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
	except:
		print("String not in Y-m-d H:M:S form")
		return None

#pre: needs datetime in Y-m-d H:M:S form
#post: returns string form
def datetime_to_string(dt_time):
	try:
		return dt_time.strftime("%Y-%m-%d %H:%M:%S")
	except:
		print("Datetime not in Y-m-d H:M:S form")
		return None
		
#pre: needs time in string and n days to be added
#post: return string with added days
def get_n_days_later(time, n):
	dt_time = string_to_datetime(time)
	dt_later = dt_time + timedelta(days = n)
	return datetime_to_string(dt_later)
	
#pre: both user must exist, client must have enough funds, and amount must be valid 
#post: transfer money from user to user.
def tranfer_funds(from_user, to_user, amount):
    if amount <= 0:
        print("Must have a positive amount")
        return 0
    if from_user.get_id() == 'Nan':
        print("The user you are grabbing from does not exist")
        return 0
    if to_user.get_id() == 'Nan':
        print("The user you are sending to does not exist")
        return 0
    if from_user.get_balance() < amount:
        print("The user does not have enough funds")
        return 0
    from_user.withdraw(amount)
    to_user.deposit(amount)
    return 1