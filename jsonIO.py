# 1.  create a json file named "DB.json"
# pre: DB is a database name - eg. projects, users ...
# post: "DB.json" file created on the same directory of this program
def create_DB(DB):
    with open(DB+'.json', 'w') as f:
        json.dump({DB:[]}, f)    # {"projects": []} 

### TEST
create_DB("projects")
# create_DB("users")
# create_DB("bids")
############################################################################

# 2-0. help function - read all rows from DB.json
# pre: DB.json exists on the same directory
# post: returns [{row1}, {row2}, ...]
def read_rows(DB):
    rows = []
    with open(DB+'.json', 'r') as f:
        rows = json.load(f)[DB]     # [{row1}, {row2}, ...]
    return rows

### TEST
# print(read_rows("projects"))
############################################################################

# 2. add a row into DB.json
# pre: 
	# DB = "projects"
	# row1 = {"projectId":11, "clientId":3, ... "status":"active"}
# post: update json file
	# DB.json = { "DB": [{row1}, {row2}, ...] } 
def add_row(DB, row):
    # read rows from json DB
    rows = read_rows(DB)

    # check if the row exists   
    for item in rows:
        if item["id"] == row["id"]: # all our database tables has a "id" attribute
            print("item already exist on the json")
            break
    else:
        # add the row
        rows.append(row)
        new_DB = {DB: rows}
        # update json
        with open(DB+'.json', 'w') as f:
            json.dump(new_DB, f)

### TEST - eg. add a project into the project.json
# project1 = {"id":11, "clientId":3, "developerId":1, "title":"project 1", "description":"testing project 1", 
#             "startDate":11012017, "endDate":11282017, "status":"active"}
# add_row("projects",project1)
# project2 = {"id":22, "clientId":4, "developerId":1, "title":"project 2", "description":"testing project 2", 
#             "startDate":10012017, "endDate":10282017, "status":"active"}
# add_row("projects", project2)
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
# post: return the id of the last row in the DB.json if there is at least one 
#       row in the DB.json. Otherwise, return None.
def get_last_id(DB):
    rows = read_rows(DB)
    if(len(rows) == 0):
        return None
    else:
        return rows[-1]["id"]
### TEST
# get_last_id("projects")        # 22
# get_last_id("users")           # None
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
get_value("projects", 22, 'status')                 # 'active'
print(set_row("projects", 22, 's', 'blacklisted'))  # None
set_row("projects", 22, 'status', 'blacklisted')
get_value("projects", 22, 'status')                 # 'blacklisted'
############################################################################