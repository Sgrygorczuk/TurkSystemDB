import json
# 1.  create a json file named "DB.json"
# pre: DB is a database name - eg. project_db, user_db, ...
# post: "DB.json" file created on the same directory of this program
def create_DB(DB):
    with open(DB+'.json', 'w') as f:
        json.dump({DB:[]}, f)    # {"project_db": []} 
        print('created '+DB+'.json')

### TEST
#create_DB("project_db")
#create_DB("user_db")
#create_DB("bid_db")
#create_DB("task_db")
#create_DB("team_db")
############################################################################

# 2-0. help function - read all rows from DB.json
# read rows from DB.json
# pre: DB.json exists on the same directory
# post: returns [{row1}, {row2}, ...] or [] if DB.json exists.
#       return None otherwise.
def read_rows(DB):
    rows = None
    try:
        with open(DB+'.json', 'r') as f:
            rows = json.load(f)[DB]     # [{row1}, {row2}, ...]
    except FileNotFoundError:
        print("file named "+DB+".json doesn't exist in the current folder." )
    return rows

### TEST
# print(read_rows("project_db")) # [{"id":11, ... },{"id":22, ...} ...] or []
# print(read_rows("not_exist"))  # None
############################################################################

# 2. add a row into DB.json
# pre: DB.json exist in the same folder. Otherwise it creates new DB.json
#      new_row is a valid row in the DB.json
# post: add the new_row into DB.json and return the new_row if all preconditions satisfies.
#       Otherwise, return None
def add_row(DB, new_row):
    # read rows from json DB
    rows = read_rows(DB)
    
    # if DB.json doesn't exist, create DB.json
    if rows == None: 
        create_DB(DB)
        rows = []
        
    # check if the row exists   
    for item in rows:
        if item["id"] == new_row["id"]: # all our database tables has a "id" attribute
            print("id:"+str(new_row["id"])+" already exist on "+DB+".json. Update using set_row(DB, id, key, new_value)")
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
# add_row("project_db",project1)
# project2 = {"id":22, "clientId":4, "developerId":1, "title":"project 2", "description":"testing project 2", 
#             "startDate":10012017, "endDate":10282017, "status":"active"}
# add_row("project_db", project2)
# add_row("new_db", project1) # creates a new_db.json and write project1 if new_db.json doesn't exist.
############################################################################

# 3. remove a row from DB.json
# pre: DB.json exist, id is a valid id for the DB
# post: A row is removed from DB.json if a row with the id exists on the DB.
#       If multiple rows with the id exists, it removes all the rows, and
#       return the number of removed rows.
#       Otherwise, there no change on DB.json, and return 0.
# remove a row from a DB
def del_row(DB, id):
    # read rows from json DB
    rows = read_rows(DB)
    
    # if DB.json doesn't exist, nothing is removed.
    if rows == None: 
        return 0 
    
    # remove a row with passed in 'id'
    filtered_rows = list(filter(lambda item: item['id'] != id, rows))
    
    # update json
    new_DB = {DB: filtered_rows}
    with open(DB+'.json', 'w') as f:
        json.dump(new_DB, f)
    
    # return the number of rows that were removed
    return len(rows)-len(filtered_rows)

### TEST 
# del_row("project_db", 11)  # 1
# del_row("not_exist", 11) # 0
############################################################################

# 4. select rows from DB.json
# pre: DB.json exist, "id" is the valid id format for the DB.json
# post: returns a row whose id is "id"
#       if no row with the "id" exists, None will be returned.
def get_row(DB, id):
    # read rows from json DB
    rows = read_rows(DB)
    if rows == None:
        return None
    
    # row with passed in 'id'
    filtered_row = list(filter(lambda item: item['id'] == id, rows))
    
    if len(filtered_row) == 0:
        return None
    else:
        return filtered_row[0] # row == {"id": id, ... }

### TEST
# get_rows("project_db", 22)       # {'id': 22,'clientId': 4, ... }
# get_rows("project_db", 111111)   # None
############################################################################

# 5. get a value that corresponds to the key from a row with the "id" in the DB.json
# pre: DB.json exist, "id" is the valid id format for the DB.json key is a string
# post: return a value from {... "key": value, ...} in DB.json if found match.
#       Otherwise, return None
def get_value(DB, id, key):
    row = get_row(DB, id)
    if(row == None):
        return None
    else:
        try:
            return row[key]
        except KeyError: # if key is not the attribute name on the DB.json
            return None
### TEST
# get_value("project_db", 22, 'status')           # 'active'
# print(get_value("project_db", 1111, 'status'))  # None
# print(get_value("project_db", 22, 's'))         # None
############################################################################

# 6. get last id
# pre: DB.json exist
# post: return the max(id) in the DB.json if there is at least one row in DB.json.
#       Otherwise, return None
def get_last_id(DB):
    rows = read_rows(DB)
    if (rows == None or len(rows) == 0):
        return None
    else:
        ids = list(map(lambda row: row["id"], rows)) # extract a list of id
        return max(ids)
### TEST
# get_last_id("project_db")      # 22
# get_last_id("not_exist")       # None
############################################################################

# 7. update a row with new value for an attribute
# pre: DB.json exist, 
#      id, key, attribute are valid in the DB
# post: if there is a row in DB like below, update the row and return the new row
#      {"id":id, "key":old_value, ... } -> {"id":id, "key":new_value, ... } 
#      Otherwise, return None
def set_value(DB, id, key, new_value):
    row = get_row(DB, id)
    if (row == None):
        return None
        
    # validate "key"
    if (key not in row.keys()):
        return None
    
    # update a row
    row[key] = new_value
    
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
# get_value("project_db", 22, 'status')                 # 'active'
# print(set_value("project_db", 22, 's', 'blacklisted'))  # None
# set_value("project_db", 22, 'status', 'blacklisted')
# get_value("project_db", 22, 'status')                 # 'blacklisted'
############################################################################
# 7-1. update a existing row with many new values
# pre: DB.json exist, new_row include 'id' attribute
# post: if there is a row in DB like below, update the row and return the new row
#      {"id":id, "key1":old_val1, "key2": old_val2 ... } -> {"id":id, "key1":new_val1, "key2": new_val2 ... } 
#      Otherwise, return None
def set_row(DB, new_row):
    # remove the old row with the same id
    removed_row = del_row(DB, new_row['id'])
    if (removed_row == 0):
        print("The row with id:"+str(new_row['id'])+" doesn't exist in "+DB+".json")
        return None
    
    # update DB
    rows = read_rows(DB)
    rows.append(new_row)

    # update json
    new_DB = {DB: rows}
    with open(DB+'.json', 'w') as f:
        json.dump(new_DB, f)

    return new_row
############################################################################

# 8. find all rows with { ... "key" : attribute ...} in DB.json
# pre: DB.json exists
#      key and value are valid in DB 
# post: return a list of rows that has key:value in DB
#       [{ ... "key" : value ...} ,  { ... "key" : value ...} , ... ]
#       if no such row exists in DB, [] will be returned.
def get_rows(DB, key, value, reversed = False):
    # read rows from json DB
    rows = read_rows(DB)
    if rows == None:
        return []
    
    # find rows whose key is value
    try:
        filtered_row = list(filter(lambda item: item[key] == value, rows))
    except KeyError:
        return []
    
    if (reversed):
        filtered_row.reverse()
        
    return filtered_row
### TEST
# get_rows("project_db", 'status', 'active')      # [{'id': 11,'clientId': 3, ... },{'id': 22,'clientId': 4, ... }]
# get_rows("project_db", 'status', 'active', True)# [{'id': 22,'clientId': 4, ... },{'id': 11,'clientId': 3, ... }]
# get_rows("project_db", 'st', 'act')             # []
############################################################################

