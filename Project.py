import jsonIO

class Project_db:
	db = "project_db"
	
	def __init__(self, client_id='Nan', bid_id='Nan', dev_ids=[], title="", desc="", start_date=0, end_date=0, status="active"):
		self.project_id = 'Nan'
		#might call new_project later on
		self.new_project(client_id, bid_id, dev_ids, title, desc, start_date, end_date, status)

	#create a new project_db
	def new_project(self, client_id, bid_id, dev_ids, title, desc, start_date, end_date, status):
		self.project_id = jsonIO.get_last_id(self.db) + 1 #last+1 for new
		jsonIO.add_row(self.db, self.project_id, client_id, bid_id, dev_ids, title, desc, start_date, end_date, status)
		self.set_all(client_id, bid_id, dev_ids, title, desc, start_date, end_date, status)
	
	def set_all(self, client_id, bid_id, dev_ids, title, desc, start_date, end_date, status):
		self.client_id = client_id
		self.bid_id = bid_id
		self.dev_ids = dev_ids
		self.title = title
		self.desc = desc
		self.start_date = start_date
		self.end_date = end_date
		self.status = status
		
	#will load db into the class (must at least set id) will return 1 or 0 upon success or failure respectively
	def load_db(self, project_id):
		if project_id != 'Nan':
			self.project_id = project_id
			self.dump(jsonIO.get_row(self.db, project_id))
			return 1
		else:
			return 0

	#breakdown the dictionary and load into the class
	def dump(self,dict):
		#self.project_id = dict["id"]
		self.set_all(dict["client_id"], dict["bid_id"], dict["dev_ids"], dict["title"],dict["desc"], dict["start_date"], dict["end_date"], dict["status"])
		
	#get_ methods
	def get_project_id(self): 
		return self.project_id
	def get_client_id(self): 
		return self.client_id
	def get_bid_id(self): 
		return self.bid_id
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
		jsonIO.set_(self.db, self.project_id, "client_id", client_id)
		return 1;
	def set_bid_id(self, bid_id):
		self.bid_id = bid_id
		jsonIO.set_(self.db, self.project_id, "bid_id", bid_id)
		return 1;
	def set_dev_ids(self, dev_ids):
		self.dev_ids = dev_ids[:]
		jsonIO.set_(self.db, self.project_id, "dev_ids", dev_ids)
		return 1;
	def set_title(self, title):
		self.title = title
		jsonIO.set_(self.db, self.project_id, "title", title)
		return 1;
	def set_desc(self, desc):
		self.desc = desc
		jsonIO.set_(self.db, self.project_id, "desc", desc)
		return 1;
	def set_start_date(self, start_date):
		self.start_date = start_date
		jsonIO.set_(self.db, self.project_id, "start_date", start_date)
		return 1;
	def set_end_date(self, end_date):
		self.end_date = end_date
		jsonIO.set_(self.db, self.project_id, "end_date", end_date)
		return 1;
	def set_status(self, status):
		self.status = status
		jsonIO.set_(self.db, self.project_id, "status", status)
		return 1;
		

#destructor
	def remove(self):
		jsonIO.del_row(self.db, self.project_id)
		print (self.project_id, ' was destroyed.')
		del self
		return 1;