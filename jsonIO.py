# 1.  create a json file named "DB.json"
# pre: DB is a database name - eg. projects, users ...
# post: "DB.json" file created on the same directory of this program
def create_DB(DB):
    with open(DB+'.json', 'w') as f:
        json.dump({DB:[]}, f)    # {"projects": []} 
        
create_DB("projects")
# create_DB("users")
# create_DB("bids")

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

    # check if the projectId exists   
    for item in rows:
        if item["id"] == row["id"]: # all our database tables has a "id" attribute
            print("item already exist on the json")
            break
    else:
        # update list of projects
        rows.append(row)
        new_DB = {DB: rows}
        # update json
        with open('projects.json', 'w') as f:
            json.dump(new_DB, f)
            
# - eg. add a project into the project.json
project1 = {"id":11, "clientId":3, "developerId":1, "title":"project 1", "description":"testing project 1", 
            "startDate":11012017, "endDate":11282017, "status":"active"}

add_row("projects",project1)
