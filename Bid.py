import jsonIO
from datetime import datetime
import copy

class Bid:
	db = "bid_db"
	now = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	
	#bid_id = project_id
	def __init__(self, project_id = 'Nan', end_date = "", initial_bid = 'Nan', bid_log = [[] for i in range(4)], comments = "", status = ""):
		#might call new_bid later on
		self.new_bid(project_id, end_date, initial_bid, bid_log, comments, status)
	
	#create a new bid in db and in class
	def new_bid(self,project_id, end_date, initial_bid, bid_log = [[] for i in range(4)], comments = "", status = "active"):
		self.set_all(end_date, initial_bid, bid_log, comments, status)
		self.id = project_id
		#make new class if not called explicitly
		if end_date:
			jsonIO.add_row(self.db, self.get_all())
	
	#create a new bid in class only
	def set_all(self, end_date, initial_bid, bid_log, comments, status, modify_db = 0):
		self.end_date = end_date
		self.final_bid = initial_bid
		if bid_log != [[]] and bid_log != None:
			self.bid_log = copy.deepcopy(bid_log) #time, bidder's id, amount, suggested end time
		else:
			self.bid_log = [[]]
		self.comments = comments
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
	def dump(self, dict):
		self.set_all(dict["end_date"], dict["final_bid"], dict["bid_log"], dict["comments"], dict["status"])
	
	#get_ methods
	def get_id(self):
		return self.id
	def get_project_id(self): 
		return self.id
	def get_end_date(self): 
		return self.end_date
	def get_final_bid(self):
		return self.final_bid
	def get_bid_log(self): 
		return self.bid_log
	def get_comments(self): 
		return self.comments
	def get_status(self): 
		return self.status
	def get_all(self):
		return {"id":self.id, "end_date":self.end_date,
		"final_bid":self.final_bid, "bid_log":self.bid_log, "comments":self.comments, "status":self.status}

	#update bid_db
	def set_id(self, id):
		jsonIO.set_value(self.db, self.id, "id", id)
		self.id = id
		return 1
	def set_project_id(self, project_id):
		self.id = project_id
		return 1
	def set_end_date(self, end_date):
		self.end_date = end_date
		jsonIO.set_value(self.db, self.id, "end_date", end_date)
		return 1
	def set_final_bid(self, final_bid):
		self.final_bid = final_bid
		jsonIO.set_value(self.db, self.id, "final_bid", final_bid)
		return 1
	#creating bid_log
	def add_bid_log(self, bidder_id, amount, suggested_time, time = now):
		if time and bidder_id != 'Nan' and amount and suggested_time:
			(self.bid_log).append({time, bidder_id, amount, suggested_time})
			jsonIO.set_value(self.db, self.id, "bid_log", self.bid_log)
			return 1
		return 0
	def set_bid_log(self, bid_log):
		if bid_log == [[]] and  bid_log != None:
			self.bid_log = copy.deepcopy(bid_log)
			jsonIO.set_value(self.db, self.id, "bid_log", self.bid_log)
			return 1
		return 0
	def set_comments(self, comments):
		self.comments = comments
		jsonIO.set_value(self.db, self.id, "comments", comments)
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