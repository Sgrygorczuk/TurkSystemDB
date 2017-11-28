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
# post: returns a [{row1}] where each rows' id is "id"
#       if no rows with the "id" exists, [] will be returned.
def get_row(DB, id):
    # read rows from json DB
    rows = read_rows(DB)
    
    # row with passed in 'id'
    filtered_row = list(filter(lambda item: item['id'] == id, rows))
    return filtered_row

### TEST
get_rows("projects", 22)
get_rows("projects", 111111) # should return []
############################################################################