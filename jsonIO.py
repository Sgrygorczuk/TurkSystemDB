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

# 2. add a row into a DB.json

# pre: 
	# DB = "projects"
	# row1 = {"projectId":11, "clientId":3, ... "status":"active"}
# post: update json file
	# DB.json = { "DB": [{row1}, {row2}, ...] } 
def add_row(DB,row):
    # read rows from json DB
    rows = []
    with open(DB+'.json', 'r') as f:
        rows = json.load(f)[DB]     # [{row1}, {row2}, ...]

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

# 3. remove a row from a DB
def del_row(DB, row):
    # read rows from json DB
    rows = []
    with open(DB+'.json', 'r') as f:
        rows = json.load(f)[DB]     # [{row1}, {row2}, ...]

    # check if the row exists   
    for item in rows:
        if item["id"] == row["id"]: # all our database tables has a "id" attribute
            # remove the row
            print('remove a row with id = ', row['id'])
            rows.remove(row)
            new_DB = {DB: rows}
            # update json
            with open(DB+'.json', 'w') as f:
                json.dump(new_DB, f)
            break
    else:
        print("the row doesn't exist in" + DB)

### TEST 
# del_row("projects", project1)
############################################################################