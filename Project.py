import jsonIO

class Project:
	db = "project_db"
	
	def __init__(self, client_id='Nan', bid_id='Nan', team_id = 'Nan', dev_ids=[], title="", desc="", start_date=0, end_date=0, status="active"):
		self.id = 'Nan'
		#might call new_project later on
		self.new_project(client_id, bid_id, team_id, dev_ids, title, desc, start_date, end_date, status)

	#create a new project in db and in class
	def new_project(self, client_id, bid_id, team_id, dev_ids, title, desc, start_date, end_date, status):
		self.id = jsonIO.get_last_id(self.db) + 1 #last+1 for new
		jsonIO.push(self.db, self.id, client_id, team_id, bid_id, team_id, dev_ids, title, desc, start_date, end_date, status)
		self.set_all(client_id, bid_id, team_id, dev_ids, title, desc, start_date, end_date, status)
	
	#create a new project in class only
	def set_all(self, client_id, bid_id, team_id, dev_ids, title, desc, start_date, end_date, status):
		self.client_id = client_id
		self.bid_id = bid_id
		self.team_id = team_id
		self.dev_ids = dev_ids
		self.title = title
		self.desc = desc
		self.start_date = start_date
		self.end_date = end_date
		self.status = status
		
	#will load db into the class (must at least set id) will return 1 or 0 upon success or failure respectively
	def load_db(self, id):
		if id != 'Nan':
			self.id = id
			self.dump(jsonIO.get_row(self.db, id))
			return 1
		else:
			return 0

	#breakdown the dictionary and load into the class
	def dump(self,dict):
		#self.id = dict["id"]
		self.set_all(dict["client_id"], dict["bid_id"], dict["team_id"], dict["dev_ids"], dict["title"], dict["desc"], dict["start_date"], dict["end_date"], dict["status"])
		
	#get_ methods
	def get_id(self): 
		return self.id
	def get_client_id(self): 
		return self.client_id
	def get_bid_id(self): 
		return self.bid_id
	def get_team_id(self): 
		return self.team_id
	def get_dev_ids(self): 
		return self.dev_ids #one or more
	def get_title(self): 
		return self.title
	def get_desc(self): 
		return self.desc
	def get_start_date(self):
		return self.start_date
	def get_end_date(self): 
		return self.end_date
	def get_status(self): 
		return self.status

	#update project_db
	def set_client_id(self, client_id):
		self.client_id = client_id
		jsonIO.set_row(self.db, self.id, "client_id", client_id)
		return 1;
	def set_bid_id(self, bid_id):
		self.bid_id = bid_id
		jsonIO.set_row(self.db, self.id, "bid_id", bid_id)
		return 1;
	def set_team_id(self, team_id):
		self.team_id = team_id
		jsonIO.set_row(self.db, self.id, "team_id", team_id)
		return 1;
	def set_dev_ids(self, dev_ids):
		self.dev_ids = dev_ids[:]
		jsonIO.set_row(self.db, self.id, "dev_ids", dev_ids)
		return 1;
	def set_title(self, title):
		self.title = title
		jsonIO.set_row(self.db, self.id, "title", title)
		return 1;
	def set_desc(self, desc):
		self.desc = desc
		jsonIO.set_row(self.db, self.id, "desc", desc)
		return 1;
	def set_start_date(self, start_date):
		self.start_date = start_date
		jsonIO.set_row(self.db, self.id, "start_date", start_date)
		return 1;
	def set_end_date(self, end_date):
		self.end_date = end_date
		jsonIO.set_row(self.db, self.id, "end_date", end_date)
		return 1;
	def set_status(self, status):
		self.status = status
		jsonIO.set_row(self.db, self.id, "status", status)
		return 1;

#destructor
	def remove(self):
		jsonIO.del_row(self.db, self.id)
		print (self.id, ' was destroyed.')
		del self
		return 1;