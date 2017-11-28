import jsonIO as jio

class bid_db:
	db = "bid_db"
	def __init__(self, client_id = 'Nan' , project_id = 'Nan', start_date = 0, end_date = 0, bid_log = [[] for i in range(3)], status = "active"):
		self.bid_id = 'Nan'
		self.set_all(client_id, project_id, start_date, end_date, bid_log, status)
		
		#create a new _db if a new project is made by initializing class
		if client_id!='Nan':
			self.new_bid(client_id, project_id, start_date, end_date, bid_log, status)
	
	#will load _db into the class (must at least set_ ID) will return 1 or 0 upon success or failure respectively
	def load_db(self):
		if self.bid_id != 'Nan':
			self.dump(jio.load_db(self.db,self.bid_id))
			return 1
		else:
			return 0
			
	#breakdown the dictionary and load into the class
	def dump(self, dict):
		#self.bid_id = dict["id"]
		self.set_all(dict["client_id"], dict["project_id"], dict["start_date"], dict["end_date"], dict["bid_log"], dict["status"])
	
	#get_ methods
	def get_bid_id(self):
		return self.bid_id
	def get_client_id(self):
		return self.client_id
	def get_project_id(self): 
		return self.project_id
	def get_start_date(self): 
		return self.start_date
	def get_end_date(self): 
		return self.end_date
	def get_bid_log(self): 
		return self.bid_log
	def get_status(self): 
		return self.status

	#create a new bid_db
	def new_bid(self, client_id, project_id, start_date, end_date, bid_log, status):
		self.bid_id = jio.get_last_id(self.db) + 1 #last+1 for new
		jio.push(self.db, self.bid_id, client_id, project_id, start_date, end_date, bid_log)
		if self.client_id!= client_id:
			self.set_all(client_id, project_id, start_date, end_date, bid_log, status)
	
	#update bid_db
	def set_all(self, client_id, project_id, start_date, end_date, bid_log, status):
		self.client_id = client_id
		self.project_id = project_id
		self.start_date = start_date
		self.end_date = end_date
		self.bid_log = bid_log #time, bidder's id, amount
		self.status = status
	def set_bid_id(self, bid_id):
		self.bid_id = bid_id
		jio.set_(self.db, self.bid_id, "id", bid_id)
		return 1;
	def set_client_id(self, client_id):
		self.client_id = client_id
		jio.set_(self.db, self.bid_id, "client_id", client_id)
		return 1;
	def set_project_id(self, project_id):
		self.project_id = project_id
		jio.set_(self.db, self.bid_id, "project_id", project_id)
		return 1;
	def set_start_date(self, start_date):
		self.start_date = start_date
		jio.set_(self.db, self.bid_id, "start_date", start_date)
		return 1;
	def set_end_date(self, end_date):
		self.end_date = end_date
		jio.set_(self.db, self.bid_id, "end_date", end_date)
		return 1;
	def set_bid_log(self, bid_log):
		self.bid_log = bid_log[:]
		jio.set_(self.db, self.bid_id, "bid_log", bid_log)
		return 1;
	def set_status(self, status):
		self.status = status
		jio.set_(self.db, self.bid_id, "status", status)
		return 1;

	def remove_bid(self):
		jio.remove(self.db, self.bid_id)
		return 1;
	
#destructor
	def __del__(self):
		raise Exception("Something went wrong when destroying")
		print (self.bid_id, ' was destroyed.')