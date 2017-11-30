import json
# 1.  create a json file named "DB.json"
# pre: DB is a database name - eg. projects, users ...
# post: "DB.json" file created on the same directory of this program
def create_DB(DB):
    with open(DB+'.json', 'w') as f:
        json.dump({DB:[]}, f)    # {"projects": []} 

### TEST
create_DB("projects_db")
#create_DB("users_db")
#create_DB("teams_db")
############################################################################

# 2-0. help function - read all rows from DB.json
# read rows from DB.json
# pre: DB.json exists on the same directory
# post: returns [{row1}, {row2}, ...] in the DB.json if DB.json exists.
#       Otherwise, return [].
def read_rows(DB):
	rows = []
	try:
		with open(DB+'.json', 'r') as f:
			if f.read():
				rows = json.load(f)[DB]     # [{row1}, {row2}, ...]
	except FileNotFoundError:
		print("file named "+DB+".json doesn't exist in the current folder." )
	return rows

### TEST
# print(read_rows("projects")) # [{"id":11, ... },{"id":22, ...} ...]
# print(read_rows("proejct"))  # []
############################################################################

# 2. add a row into DB.json
# pre: DB.json exist in the same folder. Otherwise it creates new DB.json
#      new_row is a valid row in the DB.json
# post: add the new_row into DB.json and return the new_row if all preconditions satisfies.
#       Otherwise, return None
def add_row(DB, new_row):
    # read rows from json DB
    rows = read_rows(DB)
    
    if rows == None: # if DB.json doesn't exist:
        create_DB(DB)
        rows = []
        
    # check if the row exists   
    for item in rows:
        if item["id"] == new_row["id"]: # all our database tables has a "id" attribute
            print("item already exist on the json")
            return None
    else:
        # add the row
        rows.append(new_row)
        new_DB = {DB: rows}
        # update json
        with open(DB+'.json', 'w') as f:
            json.dump(new_DB, f)
    return new_row
### TEST - eg. add a project into the project.json
# project1 = {"id":11, "clientId":3, "developerId":1, "title":"project 1", "description":"testing project 1", 
#             "startDate":11012017, "endDate":11282017, "status":"active"}
# add_row("projects",project1)
# project2 = {"id":22, "clientId":4, "developerId":1, "title":"project 2", "description":"testing project 2", 
#             "startDate":10012017, "endDate":10282017, "status":"active"}
# add_row("projects", project2)
# add_row("new_DB", project1) # creates a new_DB.json and write project1 in there
############################################################################
# 2-1. push(DB, *args)
# pre: no rows with the id on args exist in the DB.json # DB = bidDB or taskDB
# post: add a row with passed in args into DB.json and the new row is returned. 
#       if args length is different from the number of attributes of DB, returns None.
def push(DB, *args):
    new_row = None
    if (DB == "bidDB"):
        if (len(args) != 5):
            return None
        # args == [id, client_id, start_date, end_date, bid_log]
        new_row = {"id":args[0], "client_id":args[1], "start_date":args[2], "end_date":args[3], "bid_log":args[4]}
        add_row(DB, new_row)
    elif (DB == "taskDB"):
        if (len(args) != 4):
            return None
        # args == [id, user_id, issue_desc, resolved]
        new_row = {"id":args[0], "user_id":args[1], "issue_desc":args[2], "resolved":args[3]}
        add_row(DB, new_row)
    else: 
        print("push() for " + DB + " has not defined yet. - Eunjung -" )
    return new_row
### TEST - eg. add a project into the project.json
# push("bidDB", 111, 3, 10222017, 11222017, "this is test for bid 1")
# push("taskDB", 333, 2, "this user test description", "resolved")
# print(push("users", "testing", "to fail"))            # returns []
############################################################################    

# 3. remove a row from DB.json
# pre: DB.json exist, id is a valid id for the DB
# post: a row is removed from DB.json if a row with the id exists on the DB.
#       Otherwise, there no change on DB.json.
# remove a row from a DB
def del_row(DB, id):
    # read rows from json DB
    rows = read_rows(DB)
    
    # remove a row with passed in 'id'
    filtered_rows = list(filter(lambda item: item['id'] != id, rows))
    print(len(rows)-len(filtered_rows),'item was removed from '+DB)
    
    # update json
    new_DB = {DB: filtered_rows}
    with open(DB+'.json', 'w') as f:
        json.dump(new_DB, f)

### TEST 
# del_row("projects", 11)
# del_row("projects", 11) # 0 item was removed from projects.
############################################################################

# 4. select rows from DB.json
# pre: DB.json exist, "id" is the valid id format for the DB.json
# post: returns a row whose id is "id"
#       if no row with the "id" exists, None will be returned.
def get_row(DB, id):
    # read rows from json DB
    rows = read_rows(DB)
    
    # row with passed in 'id'
    filtered_row = list(filter(lambda item: item['id'] == id, rows))
    
    if (len(filtered_row) == 0):
        return None
    else:
        return filtered_row[0] # row == {"id": id, ... }

### TEST
# get_rows("projects", 22)              # {'id': 22,'clientId': 4, ... }
# print(get_rows("projects", 111111))   # None
############################################################################

# 5. get a value that corresponds to the key from a row with the "id" in the DB.json
# pre: DB.json exist, "id" is the valid id format for the DB.json key is a string
# post: return a value from {... "key": value, ...} in DB.json
def get_value(DB, id, key):

    row = get_row(DB, id)

    if(row == None):
        return None
    else:
        try:
            return row[key]
        except KeyError:
            return None
### TEST
# get_value("projects", 22, 'status')           # 'active'
# print(get_value("projects", 1111, 'status'))  # None
# print(get_value("projects", 22, 's'))         # None
############################################################################

# 6. get last id
# pre: DB.json exist
# post: return the max(id) in the DB.json if there is at least one row in DB.json.
#       Otherwise, return 0.
def get_last_id(DB):
    rows = read_rows(DB)
    if (len(rows) == 0):
        return 0
    else:
        ids = list(map(lambda row: row["id"], rows)) # extract a list of id
        return max(ids)
### TEST
# get_last_id("projects")        # 22
# get_last_id("users")           # 0
############################################################################

# 7. update a row with new value for an attribute
# pre: DB.json exist, 
#      id, key, attribute are valid in the DB
# post: if there is a row in DB like below, update a row of DB and return the new row
#      {"id":id, "key":old_attribute, ... } -> {"id":id, "key":new_attribute, ... } 
#      Otherwise, return None
def set_row(DB, id, key, new_attribute):
    row = get_row(DB, id)
    if (row == None):
        return None
    else:
        # validate "key"
        if (key not in row.keys()):
            return None
        
        # update a row
        row[key] = new_attribute
        
        # update DB
        del_row(DB, id)
        rows = read_rows(DB)
        rows.append(row)
        
        # update json
        new_DB = {DB: rows}
        with open(DB+'.json', 'w') as f:
            json.dump(new_DB, f)

        return row
### TEST
# get_value("projects", 22, 'status')                 # 'active'
# print(set_row("projects", 22, 's', 'blacklisted'))  # None
# set_row("projects", 22, 'status', 'blacklisted')
# get_value("projects", 22, 'status')                 # 'blacklisted'
############################################################################

# 8. find all rows with { ... "key" : attribute ...} in DB.json
# pre: DB.json exists
#      key and attribute are valid in DB 
# post: return a list of rows that has attribute as its key value in DB
#       [{ ... "key" : attribute ...} ,  { ... "key" : attribute ...} , ... ]
#       if no such row exists in DB, [] will be returned.
def get_rows(DB, key, attribute, reversed = False):
    # read rows from json DB
    rows = read_rows(DB)
    
    # find rows whose key value is attribute
    try:
        filtered_row = list(filter(lambda item: item[key] == attribute, rows))
    except KeyError:
        return []
    
    if (reversed):
        filtered_row.reverse()
    return filtered_row
### TEST
# get_rows("projects", 'status', 'active')      # [{'id': 11,'clientId': 3, ... },{'id': 22,'clientId': 4, ... }]
# get_rows("projects", 'status', 'active', True)# [{'id': 22,'clientId': 4, ... },{'id': 11,'clientId': 3, ... }]
# get_rows("projects", 'st', 'act')             # []
############################################################################

