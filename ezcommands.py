from User import *
from Project import *
from Team import *
from Bid import *
from Issue import *
from jsonIO import *
import os
import shutil
import inspect
import numpy

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")

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
#post: prints all available commands
def get_commands():
	print ('''-------------------------------------------------------------------------------------
Direct Databse access
	get_value(obj, key, id = 'Nan'): gets value
	get_all_db(obj): gets all from db
	get_row(obj, key): gets an entire row
	print_table(m): prints the table given a dictionary or a list of it
-------------------------------------------------------------------------------------
SU
	user_report(user, id = 'Nan'): returns status of the user:
		user_type, status, warning, and balance
	verify(username, password = ""): returns [case number, user, message]
	*not made*project_completion : decides what to do after project is completed
		users rate each other:
				what to do with bid money
				blaklist users
		and other modifications
	quit_request: user is removed and will call quit_team
	quit_team: doesnt matter if admin or user, but will kick devs if he's last admin
		and update their team_ids
-------------------------------------------------------------------------------------
Class creation
	user_exists(username): returns 1 if user exist else returns 0
	register_user(name, username, password, user_type, deposit):
		places new temp_user in SU tasks
	create_bid(project_id, end_date, initial_bid, start_date = now):
	
	create_project(client_id, title, desc, deadline):
		will return and make a new project
	create_bid(project_id, end_date, initial_bid, start_date = now): returns a new bid
	*not made*create_issue()
-------------------------------------------------------------------------------------
Special functions
	project_fund_transfer(from_user_id, to_user_id, amount): it will modify both 
		 balances and create task. Check below for more details.
	erase_empty_team(team_id): will delete team if there is no admin and return true
		will also kick developers out and update their team_id to 'Nan'
        else it will return false
	kick(team_dict, user_id):  will remove user from team and update both user and team db
	request_join(team_dict, user_id):  will add user to the team and update team's dev_ids
	accept_team(team_dict, user_id): user's team_id will be updated and team's request list will shrink
	reject_team(team_dict, user_id): team's request list will shrink
	*not made*start_bid
	*not made*bid_process
	*not made*end_bid: make needed modifications such as penalty or set_team_id
	*not made*rate
-------------------------------------------------------------------------------------
Metrics
	get_grade(obj,user,dic=false): returns the average rating of dev, team, or client
	get_total_commision(obj,user,dic=false): returns the money made 
		by all projects from user/ team
-------------------------------------------------------------------------------------
Helper functions
	find_row(db, key, value): returns row of given key value
	val_print(values): support method for print_table method
	get_time(): returns current date time in Y-m-d H:M:S form
	string_to_datetime(time): returns datetime form
	datetime_to_string(dt_time): returns string form
	get_n_days_later(time, n): return string with added days 
	tranfer_funds(from_user, to_user, amount): it will modify both balances
	is_admin(dic): returns true if user is team admin
	promote(team_dict, user_id): user becomes admin in team
	demote(team_dict, user_id): admin becomes user
	get_files(src, file = None, dst = os.getcwd(), username = None,
		init_path = "C:/Users/username/Desktop"):
		will either return available files if file not stated
		else copies a new file from folder to folder''')
#############################################################################

#/\/\/\/\DIRECT DATABASE ACCESS/\/\/\/\DIRECT DATABASE ACCESS/\/\/\/\DIRECT DATABASE ACCESS/\/\/\/\

#pre: given an instance of a class, key, and id (unless id is initialized in object)
#post: get attribute from a class 
#	   else return 'Nan'
#ex: get_value(User(), "name", 0)
#	 returns: System Admit
def get_value(obj, key, id = 'Nan'):
    if id == 'Nan':
        id = obj.get_id()
        if not key:
            print("Key not stated")
            return 'Nan'
        elif id == 'Nan':
            print("ID not initialized")
            return 'Nan'
        else:
            #can pull from user
            method = 'get_'+key
            try:
                value = getattr(obj, method)()
                return value
            except:
                print("No such key exist")
                return 'Nan'
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
#      else return {}
def get_row(obj, id = 'Nan'):
	if id == 'Nan':
		id = obj.get_id()
		if id == 'Nan':
			print("ID not initialized")
			return {}
		else:
			#can pull from user
			return obj.get_all()
	elif isinstance(id, str):
		print("ID does not exits")
		return {}
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
#else returns {}
def user_report(user, id = 'Nan'):
	if user.__class__ != User:
		print("User is not of type User")
		return {}
	if id == 'Nan':
		id = user.get_id()
		if id == 'Nan':
			print("ID not initialized")
			return {}
		else:
			#can pull from user
			return {"user_type":user.get_user_type(), "status":user.get_status(),
			"warning":user.get_warning(), "balance":user.get_balance()}
	obj = jsonIO.get_row(user.db, id)
	if obj == None:
		return {}
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
		elif user["status"] == "inactive":
			case = 5
			message = "User found but deactivated"
		elif password == None:
			if user["warning"] == 2:
				if user["status"] != "blacklisted":
					case = 6
					message = "User found, but has 2 warnings and not yet black listed"
				#blacklisted already checked
			elif user["status"] == "rejected":
				case = 7
				message = "Temporary user found, but was rejected and password"
			else:
				case = 8
				message = "User found and has no warnings, password not yet verified"
		#check with password
		elif user["password"] != password:
			case = 9
			message = "Your password does not match"
		elif user["warning"] == 2:
			if user["status"] != "blacklisted":
				case = 10
				message = "Login successful, but has 2 warnings and not yet black listed"
		elif user["status"] == "rejected":
				case = 11
				message = "Login successful, but temporary user was rejected"
		else: #user["password"] matches
			case = 0
			message = "Login successful"
	print(message)
	return [case, user, message]
	
#cond:
#pre:#check if balance == 0
	#check if warnings == 2, then
    #check if in the middle of a project
#post:
	#if not in middle of project
		#remove from team (admin/dev_ids)
		#remove from project (client)
	#modify user status
	#modify task (approved/denied)
def quit_request(issue_id):
    issue = jsonIO.get_row("issue_db", issue_id)
    if not issue:
        print ("The issue you are grabbing from does not exist")
        return ""
    user_id = issue["referred_id"]
    user = User()
    user.load_db(user_id)
    message = ""
    #check user_id exist
    if user.get_id() == 'Nan':
        print ("The user you are grabbing from does not exist")
        return ""
    #check if balance == 0
    if user.get_balance() != 0:
        message = "The user has unresolved balance (balance is not 0)"
    #check if warnings == 2
    elif user.get_warning == 2:
        message = "The user is or will be blacklisted"
    #check if in the middle of a project
    else:
        if user.get_project_ids():
            project = jsonIO.get_row("project_db", user.get_project_ids()[-1])
            if project["status"] == "active":
                message = "The user is in the middle of a project"
            #check if client is managing a bid
            elif user.get_user_type() == "client":
                if jsonIO.get_value("bid_db", project["id"], "status") == "active":
                    message = "The client is in the middle of a bid"
            #remove from team (admin/dev_ids)
            elif user.get_team_id():
                quit_team(user_id)
    if not message:
        message = "Done"
    #modify user status
    jsonIO.set_value("user_db", user_id, "status", "inactive") 
    #MUST modify the issue
    issue["admin_review"] = message
    issue["date_resolved"] = now
    issue["resolved"] = True
    jsonIO.set_row("issue_db", issue)
    return message
	
#cond: will delete user but wont update the issue_db
#pre: user_id must exist
#	  must not be in the middle of a project
#     must belong to a team
#post: will quit the team and will kick out devs if 
#      this admin was the last one
def quit_team(user_id):
	user = jsonIO.get_row("user_db", user_id)
	message = ""
	if not user:
		print ("User does not exist")
		return ""
	#check if in the middle of a project
	if user["project_ids"]:
		if jsonIO.get_value("project_db", user["project_ids"][-1], "status") == "active":
			message = "The user is in the middle of a project"
			return message
	#check if user is in team
	team = jsonIO.get_row("team_db", user["team_id"])
	if not team:
		print ("User does not belong to a team")
		return ""
	#if it is an admit, remove him
	for admin in team["admin_ids"]:
		if admin == user_id:
			jsonIO.set_value("team_db", team["id"], "admin_ids",
							team["admin_ids"].remove(user_id))
	#support function see bottom
	#delete if he was the last admin and kick devs out
	if not erase_empty_team(team["id"]):
		#team not yet erased
		for dev in team["dev_ids"]:
			if dev == user_id:
				jsonIO.set_value("team_db", team["id"], "dev_ids", team["dev_ids"].remove(user_id))
	#modify user team_id to 'Nan'
	jsonIO.set_value("user_db", user_id, "team_id", 'Nan')
	if message == "":
		message = "Done"
	return message


#/\/\/\/\CLASS CREATION/\/\/\/\CLASS CREATION/\/\/\/\CLASS CREATION/\/\/\/\

#pre: none
#post: returns 1 if user exist else returns 0
def user_exists(username):
    return 1 if find_row("user_db", "username", username) else 0

#pre: takes required attribute of new user, username should not exist
#post: places new temp_user in SU issues or return message
def register_user(name, username, password, user_type, deposit):
    #empty inputs
    if username == "":
        return "Username field is empty"
    elif user_exists(username):
        return "That username already exists"
    elif password == "":
        return "Password field is empty"
    elif name == "":
        return "Name field is empty"
    #check values
    elif len(password) > 64:
        return "That password is too long"
    elif len(name) > 80:
        return "That name is too long"
    elif not name.isalpha():
        return "That name has numbers or special charaters"
    elif user_type != "client" and user_type != "dev" and user_type!= "SU":
        return "That is not a valid user type"
    #see if deposit is a positive integer
    else:
        try:
            val = float(deposit)
            #check deposit amount
            if val <= 0:
                return "The deposit is too low"
            #check deposit syntax
            val = str(deposit)
            if '.' in val:
                if len(val.rsplit('.')[-1]) > 2:
                    return "That is not a valid deposit"
            #create User and Ussue
            print ("User made")
            user = User(name = name, username = username, password = password, user_type = user_type, balance = float(deposit), status = "temp")
            Issue(user.get_id(),"new user")
            return user.get_all()
        #this was when deposit was not right syntax
        except ValueError:
            return "That is not a valid deposit"

#pre: needs all the entries filled and an existing client id
#post: will return and make a new project, and add project_id to client
def create_project(client_id, title, desc, deadline):
	#check empty
	if title == "":
		return "Title field is empty"
	if desc == "":
		return "Description field is empty"
	if deadline == "":
		return "End date field is empty"
	if not find_row("user_db","id", client_id):
		print("User not found")
		return 'Nan'
	#make sure string is a valid date
	#uses helper_function
	e_date = string_to_datetime(deadline)
	if not e_date:
		return 'Nan'
	#make sure end time > start time 
	if dt_now >= e_date:
		return "The end date must be after the start date"
	project = Project(client_id, title, desc, deadline)
	client = User()
	client.load_db(client_id)
	client.add_project_ids(project.get_id())
	return project

#pre: must have client and project id for input and bid_id must be new
#    end>start date and client's balance >= bid
#post: returns a new bid
def create_bid(project_id, end_date, initial_bid, start_date = now):
	#check empty
	if start_date == "":
		print("Start date field is empty")
		return 'Nan'
	if end_date == "":
		return "End date field is empty"
	#check amount is positive
	if initial_bid < 0:
		return "Initial bid must be positive"
	#check id consistencies
	project = jsonIO.get_row("project_db", project_id)
	if not project:
		print("Project not found")
		return 'Nan'
	bid = jsonIO.get_row("bid_db", project_id)
	if bid:
		print("Bid already exists")
		return 'Nan'
	user = jsonIO.get_row("user_db", project["client_id"])
	if not user:
		print("User not found")
		return 'Nan'
	#make sure client has money
	if float(user["balance"]) < initial_bid:
		return "User does not have enough funds"
	#make sure end time > start time
	#uses helper_function
	s_date = string_to_datetime(start_date)
	e_date = string_to_datetime(end_date)
	#make sure string is a valid date
	#uses helper_function
	if not s_date or not e_date:
		return 'Nan'
	if s_date >= e_date:
		return "The end date must be after the start date"
	return Bid(project_id, [start_date, user["id"], initial_bid, end_date])
	
	
#/\/\/\/\SPECIAL FUNCTIONS/\/\/\/\SPECIAL FUNCTIONS/\/\/\/\SPECIAL FUNCTIONS/\/\/\/\ 

#cond: this is called at the beginning after the bid is done
#      the SU will withdraw the money and take 10% then give
#      half of the money to the team, and will add to SU issues.
#      It will be set as resolved, and set as unresolved when
#      the team submits their work or until the deadline.
#pre: from, to users exist and amount exists and is valid
#post: it will modify both balances and create issue.
def project_fund_transfer(from_user_id, to_user_id, amount):
	from_user = User()
	to_user = User()
	from_user.load_db(from_user_id)
	to_user.load_db(to_user_id)
	if amount <= 0:
		return "Must have a positive amount"
	if from_user.get_id() == 'Nan':
		print("The user you are grabbing from does not exist")
		return 'Nan'
	if (to_user.get_id() == 'Nan' or to_user.get_status() == "blacklisted" or
		to_user.get_status() == "inactive" or to_user.get_status() == "rejected"):
		return "The user you are sending to does not exist"
	if from_user.get_balance() < amount:
		return "The user does not have enough funds"
	if not from_user.get_project_ids:
		return "The client has not initiated a project"
	#create a new Issue after money transfers
	from_user.withdraw(amount)
	#take 10% and take 50% until completion of project
	deduction = round(amount*.1*.5, 2)
	amount -= deduction
	#keep it in superuser's bank
	jsonIO.set_value("user_db", 0, "balance", deduction)
	to_user.deposit(amount)
	#create a new issue to retrieve the other 40% = 50%-10# fee
	return Issue(from_user.get_project_ids[-1], "new project", True)
	
#cond: will erase if there is no admin and return a truth
#pre: the team_id is valid
#post: will delete team if there is no admin and return true
#      will also kick developers out and update their team_id to 'Nan'
#      else it will return false
def erase_empty_team(team_id):
	team = jsonIO.get_row("team_db", team_id)
	if not team:
		print ("Team does not exist")
		return 0
	if team["admin_ids"]:
		return 0
	if team["dev_ids"]:
		for dev_id in team["dev_ids"]:
			jsonIO.set_value("user_db", dev_id, "team_id", 'Nan')
	jsonIO.del_row("team_db", team_id)
	return 1

#pre: team and user must exit
#pro: will remove user from team and update both user and team db
def kick(team_dict, user_id):
	team_dict["dev_ids"].remove(user_id)
	user = jsonIO.get_row("user_db", user_id)
	if user:
		if is_admin(user):
			team_dict["admin_ids"].remove(user_id)
		user["team_id"] = "Nan"
		set_row("user_db", user)
		set_row("team_db", team_dict)
		return 1
	print("User does not exist")
	return 0

#pre:  team and user must exist
#post: will add user to the team and update team's dev_ids
def request_join(team_dict, user_id):  
	team_dict["join_request_ids"].append(user_id)
	user = jsonIO.get_row("user_db", user_id)
	if user:
		user["team_id"] = team_dict["id"]
		print(user["team_id"])
		set_row("user_db", user)
		set_row("team_db", team_dict)
		return user
	print("User does not exist")
	return 'Nan'

#cond: accepts the user from the join request list
#pre: team and user exists
#post: user's team_id will be updated and team's request list will shrink
def accept_team(team_dict, user_id):
	team_dict["dev_ids"].append(user_id)
	team_dict["join_request_ids"].remove(user_id)
	user = jsonIO.get_row("user_db", user_id)
	user["team_id"] = team_dict["id"]
	set_row("user_db", user)
	set_row("team_db", team_dict)

#cond: rejects the user from the join request list
#pre: team and user exists
#post: team's request list will shrink
def reject_team(team_dict, user_id):
	team_dict["join_request_ids"].remove(user_id)
	user = jsonIO.get_row("user_db", user_id)
	user["team_id"] = "Nan"
	set_row("user_db", user)
	set_row("team_db", team_dict)

#/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\
#cond: dev    avg (dev,"team")
#      team   avg (team,"team")
#      client avg (client, "client")
#pre: id must exists for all 
#post: return average rate
def get_grade(obj, user, dict = False):
	grade = []
	user+="_rating"
	#grade for class
	if not dict:
		if ((obj.get_user_type() == "client" and user == "client") or 
			(obj.get_user_type() != "client"  and user == "team")):
			for id in obj.get_project_ids():
				grade.append(jsonIO.get_value("project_db", id, user))
		else:
			print ("Use types don't match")
	#grade for dict
	else:
		if ((obj["get_user_type"] == "client" and user == "client") or 
			(obj["get_user_type"] != "client"  and user == "team")):
			for id in obj["project_ids"]:
				grade.append(jsonIO.get_value("project_db", id, user))
		else:
			print ("Use types don't match")
	#if rate exist return something
	if grade:
		return round(numpy.mean(grade), 2)
	return 'Nan'
	
#cond: dev    total (dev)
#      team   total (team)
#pre: id must exists for all 
#post: return total comssion
def get_total_commision(obj, dict = 0):
    commision = 0
    #commision for class
    if not dict:
        for id in obj.get_project_ids():
            #bid_id = project_id
            bid = jsonIO.get_value("bid_db", id, "final_bid")
            if bid:
                commision += bid
    #commision for dict
    else:
        for id in obj["project_ids"]:
            #bid_id = project_id
            bid = jsonIO.get_value("bid_db", id, "final_bid")
            if bid:
                commision += bid
    #if commision exist return something
    return commision
	
	
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
		return 'Nan'
		
#pre: needs time in string and n days to be added
#post: return string with added days
def get_n_days_later(time, n):
	dt_time = string_to_datetime(time)
	dt_later = dt_time + timedelta(days = n)
	return datetime_to_string(dt_later)
	
#pre: both user must exist, client must have enough funds, and amount must be valid 
#post: transfer money from user to user.
def tranfer_funds(from_user_id, to_user_id, amount):
	from_user = User()
	to_user = User()
	from_user.load_db(from_user_id)
	to_user.load_db(to_user_id)
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

#pre: user must exist
#pro: check if user is active
def is_in_active_project(user):
   if len(user["project_ids"]) > 0:
	   id = user["project_ids"][len(user["project_ids"]) - 1]
	   project = jsonIO.get_row("project_db", id)
	   if project["status"] == "active":
		   return True
	   else:
		   return False
   return False
  
#cond: dict will contain a dict of user (has "team_id and id")
#pre: team_id must exits
#post: returns team admin
def is_admin(dict):
   if dict["team_id"] == "Nan":
	   return False
   else:
	   team = get_row(Team(), dict["team_id"])
	   for admin in team["admin_ids"]:
		   if dict["id"] == admin:
			   return True

#post: user becomes admin in team
def promote(team_dict, user_id):
   team_dict["admin_ids"].append(user_id)
   set_row("team_db", team_dict)

#post: admin becomes user
def demote(team_dict, user_id):
   team_dict["admin_ids"].remove(user_id)
   set_row("team_db", team_dict)
  
#cond:  if file is not defined, it will just print what is in the path
#		if file is defined we copy the file to to_path
#		if username is defined, we use the init_path
#       if to_path does not exist, it will create it
#pre: needs valid path
#post: will either return available files if file not stated
#   else copies a new file
def get_files(src, file = None, dst = os.getcwd(), username = None, init_path = "C:/Users/username/Desktop"):
	#if a username is defined use it as a initial_path, so path = initial_path + path
	if username:
		init_path = init_path.replace("username", username)
		src = init_path+"/"+src
	#if only path it will print availble files
	if not file:
		list = os.listdir(src)
		print (list)
		return list
	if not os.path.exists(os.path.join(src,file)):
		print("The file path:", os.path.join(src,file), "does not exist")
		return "Nan"
	if not os.path.exists(dst):
		print("Directory does not exist, so making a new one")
		os.mkdir(dst)
	print("File copied")
	return shutil.copy(os.path.join(src, file), dst)