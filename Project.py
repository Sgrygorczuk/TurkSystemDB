import jsonIO

class Project:
	db = "project_db"
	
	def __init__(self, client_id='Nan', title="", desc="", deadline="", bid_end_date="",
		team_id = 'Nan', bid_id='Nan', client_rating = 0, team_rating = 0, rating_review = 0, status=""):
		self.id = 'Nan'
		#might call new_project later on
		self.new_project(client_id, title, desc, deadline, bid_end_date, team_id, bid_id, client_rating, team_rating, rating_review, status)

	#create a new project in db and in class
	def new_project(self, client_id, title, desc, deadline, bid_end_date = "",
		team_id = 'Nan', bid_id='Nan', client_rating = 0, team_rating = 0, rating_review = 0, status = "active"):
		self.set_all(client_id, title, desc, deadline, bid_end_date, team_id, bid_id, client_rating, rating_review, team_rating, status)
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
	def set_all(self, client_id, title, desc, deadline, bid_end_date, team_id, bid_id, client_rating, team_rating, rating_review, status, modify_db = 0):
		self.client_id = client_id
		self.title = title
		self.desc = desc
		self.deadline = deadline
		self.bid_end_date = bid_end_date
		self.team_id = team_id
		self.bid_id = bid_id
		self.client_rating = client_rating
		self.team_rating = team_rating
		self.rating_review = rating_review
		self.status = status
		if modify_db:
			jsonIO.set_row(self.db, self.get_all())
		
	#will load db into the class (must at least set id) will return 1 or 0 upon success or failure respectively
	def load_db(self, id):
		array = jsonIO.get_row(self.db, id)
		if array:
			self.id = id
			self.dump(array)
			return array
		else:
			return []

	#breakdown the dictionary and load into the class
	def dump(self,dict):
		self.set_all(dict["client_id"], dict["title"], dict["desc"], dict["deadline"], dict["bid_end_date"],
		dict["team_id"], dict["bid_id"], dict["client_rating"], dict["team_rating"], dict["rating_review"], dict["status"])
		
	#get_ methods
	def get_id(self): 
		return self.id
	def get_client_id(self): 
		return self.client_id
	def get_title(self): 
		return self.title
	def get_desc(self): 
		return self.desc
	def get_deadline(self):
		return self.deadline
	def get_bid_end_date(self): 
		return self.bid_end_date
	def get_team_id(self): 
		return self.team_id
	def get_bid_id(self): 
		return self.bid_id
	def get_client_rating(self): 
		return self.client_rating
	def get_team_rating(self): 
		return self.team_rating
	def get_rating_review(self):
		return self.rating_review
	def get_status(self): 
		return self.status
	def get_all(self):
		return {"id":self.id, "client_id":self.client_id, "title":self.title, "desc":self.desc, "deadline":self.deadline, "bid_end_date":self.bid_end_date,
		"team_id":self.team_id, "bid_id":self.bid_id, "client_rating":self.client_rating, "team_rating":self.team_rating, "rating_review": self.rating_review, "status":self.status}
	
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
	def set_deadline(self, deadline):
		self.deadline = deadline
		jsonIO.set_value(self.db, self.id, "deadline", deadline)
		return 1
	def set_bid_end_date(self, bid_end_date):
		self.bid_end_date = bid_end_date
		jsonIO.set_value(self.db, self.id, "bid_end_date", bid_end_date)
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
		if client_rating <= 5 and client_rating >= 1:
			self.client_rating = client_rating
			jsonIO.set_value(self.db, self.id, "client_rating", client_rating)
			return 1
		else:
			print(client_rating, " is not a valid entry, rating must be between 1 and 5")
			return 0
	def set_team_rating(self, team_rating):
		if team_rating <= 5 and team_rating >= 1:
			team_rating = team_rating
			jsonIO.set_value(self.db, self.id, "team_rating", team_rating)
			return 1
		else:
			print(team_rating, " is not a valid entry, rating must be between 1 and 5")
			return 0
	def set_rating_review(self, rating_review):
		self.rating_review = rating_review
		jsonIO.set_value(self.db, self.id, "rating_review", rating_review)
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