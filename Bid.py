import jsonIO
from datetime import datetime

class Bid:
	db = "bid_db"
	now = str(datetime.now())
	
	#bid_id = project_id
	def __init__(self, project_id = 'Nan', start_date = "", end_date = "", final_bid = 'Nan', bid_log = [[] for i in range(3)], status = ""):
		#might call new_bid later on
		self.new_bid(project_id,start_date, end_date, final_bid, bid_log, status)
	
	#create a new bid in db and in class
	def new_bid(self,project_id, start_date, end_date, final_bid = 'Nan', bid_log = [[] for i in range(3)], status = "active"):
		self.set_all(start_date, end_date, final_bid, bid_log, status)
		self.id = project_id
		#make new class if not called explicitly
		if start_date:
			jsonIO.add_row(self.db, self.get_all())
	
	#create a new bid in class only
	def set_all(self, start_date, end_date, final_bid, bid_log, status, modify_db = 0):
		self.start_date = start_date
		self.end_date = end_date
		self.final_bid = final_bid
		self.bid_log = bid_log #time, bidder's id, amount
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
	def dump(self, dict):
		self.set_all(dict["start_date"], dict["end_date"], dict["final_bid"], dict["bid_log"], dict["status"])
	
	#get_ methods
	def get_id(self):
		return self.id
	def get_project_id(self): 
		return self.id
	def get_start_date(self): 
		return self.start_date
	def get_end_date(self): 
		return self.end_date
	def get_final_bid(self):
		return self.final_bid
	def get_bid_log(self): 
		return self.bid_log
	def get_status(self): 
		return self.status
	def get_all(self):
		return {"id":self.id, "start_date":self.start_date, "end_date":self.end_date,
		"final_bid":self.final_bid, "bid_log":self.bid_log, "status":self.status}

	#update bid_db
	def set_id(self, id):
		jsonIO.set_value(self.db, self.id, "id", id)
		self.id = id
		return 1
	def set_project_id(self, project_id):
		self.id = project_id
		return 1
	def set_start_date(self, start_date):
		self.start_date = start_date
		jsonIO.set_value(self.db, self.id, "start_date", start_date)
		return 1
	def set_end_date(self, end_date):
		self.end_date = end_date
		jsonIO.set_value(self.db, self.id, "end_date", end_date)
		return 1
	#creating bid_log
	def add_bid(self, bidder_id, amount, time = now):
		set_bid_log(self.bid_log.append({bidder_id, amount, time}))
		return 1
	def set_bid_log(self, bid_log):
		self.bid_log = bid_log[:]
		jsonIO.set_value(self.db, self.id, "bid_log", bid_log)
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