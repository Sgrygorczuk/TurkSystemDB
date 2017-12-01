import jsonIO

class Project:
	db = "project_db"
	
	def __init__(self, client_id='Nan', title="", desc="", start_date="", end_date="",
		team_id = 'Nan', bid_id='Nan', client_rating = 0, team_rating = 0, status=""):
		self.id = 'Nan'
		#might call new_project later on
		self.new_project(client_id, title, desc, start_date, end_date, team_id, bid_id, client_rating, team_rating, status)

	#create a new project in db and in class
	def new_project(self, client_id, title, desc, start_date, end_date,
		team_id = 'Nan', bid_id='Nan', client_rating = 0, team_rating = 0, status="active"):
		self.set_all(client_id, title, desc, start_date, end_date, team_id, bid_id, client_rating, team_rating, status)
		#make new class if not called explicitly
		if title:
			self.id = jsonIO.get_last_id(self.db)
			#if no ids were made
			#if no ids made
			if self.id == None:
				self.id = 0
			else:
				self.id += 1 #last+1 for new
			jsonIO.add_row(self.db, self.get_all())
	
	#create a new project in class only
	def set_all(self, client_id, title, desc, start_date, end_date, team_id, bid_id, client_rating, team_rating, status, modify_db = 0):
		self.client_id = client_id
		self.title = title
		self.desc = desc
		self.start_date = start_date
		self.end_date = end_date
		self.team_id = team_id
		self.bid_id = bid_id
		self.client_rating = client_rating
		self.team_rating = team_rating
		self.status = status
		if modify_db:
			jsonIO.set_row(self.db, self.get_all())
		
	#will load db into the class (must at least set id) will return 1 or 0 upon success or failure respectively
	def load_db(self, id):
		array = jsonIO.get_row(self.db, id)
		if array:
			self.id = id
			self.dump(array)
			return 1
		else:
			return 0

	#breakdown the dictionary and load into the class
	def dump(self,dict):
		self.set_all(dict["client_id"], dict["title"], dict["desc"], dict["start_date"], dict["end_date"],
		dict["team_id"], dict["bid_id"], dict["client_rating"], dict["team_rating"], dict["status"])
		
	#get_ methods
	def get_id(self): 
		return self.id
	def get_client_id(self): 
		return self.client_id
	def get_title(self): 
		return self.title
	def get_desc(self): 
		return self.desc
	def get_start_date(self):
		return self.start_date
	def get_end_date(self): 
		return self.end_date
	def get_team_id(self): 
		return self.team_id
	def get_bid_id(self): 
		return self.bid_id
	def get_client_rating(self): 
		return self.client_rating
	def get_team_rating(self): 
		return self.team_rating
	def get_status(self): 
		return self.status
	def get_all(self):
		return {"id":self.id, "client_id":self.client_id, "title":self.title, "desc":self.desc, "start_date":self.start_date, "end_date":self.end_date,
		"team_id":self.team_id, "bid_id":self.bid_id, "client_rating":self.client_rating, "team_rating":self.team_rating, "status":self.status}
	
	#update project_db
	def set_client_id(self, client_id):
		self.client_id = client_id
		jsonIO.set_value(self.db, self.id, "client_id", client_id)
		return 1
	def set_title(self, title):
		self.title = title
		jsonIO.set_value(self.db, self.id, "title", title)
		return 1
	def set_desc(self, desc):
		self.desc = desc
		jsonIO.set_value(self.db, self.id, "desc", desc)
		return 1
	def set_start_date(self, start_date):
		self.start_date = start_date
		jsonIO.set_value(self.db, self.id, "start_date", start_date)
		return 1
	def set_end_date(self, end_date):
		self.end_date = end_date
		jsonIO.set_value(self.db, self.id, "end_date", end_date)
		return 1
	def set_team_id(self, team_id):
		self.team_id = team_id
		jsonIO.set_value(self.db, self.id, "team_id", team_id)
		return 1
	def set_bid_id(self, bid_id):
		self.bid_id = bid_id
		jsonIO.set_value(self.db, self.id, "bid_id", bid_id)
		return 1
	def set_client_rating(self, client_rating):
		self.client_rating = client_rating
		jsonIO.set_value(self.db, self.id, "client_rating", client_rating)
		return 1
	def set_team_rating(self, team_rating):
		team_rating = team_rating
		jsonIO.set_value(self.db, self.id, "team_rating", team_rating)
		return 1
	def set_status(self, status):
		self.status = status
		jsonIO.set_value(self.db, self.id, "status", status)
		return 1

#destructor
	def remove(self):
		jsonIO.del_row(self.db, self.id)
		print (self.id, ' was destroyed.')
		del self
		return 1