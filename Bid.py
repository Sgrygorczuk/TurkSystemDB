import jsonIO
from datetime import datetime
import copy

class Bid:
	db = "bid_db"
	now = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	
	#bid_id = project_id
	def __init__(self, project_id = 'Nan', bid_log = [[]], chosen_index = 'Nan', client_review = ""):
		#might call new_bid later on
		self.new_bid(project_id, bid_log, chosen_index, client_review)
	
	#create a new bid in db and in class
	def new_bid(self, project_id, bid_log, chosen_index = 'Nan', client_review = ""):
		self.set_all(bid_log, chosen_index, client_review)
		self.id = project_id								#bid_id = project_id
		#make new class if not called explicitly
		if bid_log != [[]] and bid_log:
			jsonIO.add_row(self.db, self.get_all())
	
	#create a new bid in class only
	def set_all(self, bid_log, chosen_index, client_review, modify_db = 0):
		#must not be empty list of list, must not be None, must have a list of list
		if bid_log != [[]] and bid_log and any(isinstance(bid, list) for bid in bid_log):
			if any(len(bid) != 4 for bid in bid_log):
				print("bid_log must contain 4 entries within another list")
				self.bid_log = [[]]
			else:
				self.bid_log = copy.deepcopy(bid_log) 	#time, bidder's id, amount, suggested end time
		else:
			self.bid_log = [[]]
		self.chosen_index = chosen_index				#this will be the index that the client chose (winning bid)
		self.client_review = client_review				#this will be to explain the choice client made
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
		self.set_all(dict["bid_log"], dict["chosen_index"], dict["client_review"])
	
	#get_ methods
	def get_id(self):
		return self.id
	def get_project_id(self): 
		return self.id
	def get_bid_log(self): 
		return self.bid_log
	def get_chosen_id(self): 
		return self.chosen_index
	def get_client_review(self): 
		return self.client_review
	def get_all(self):
		return {"id":self.id, "bid_log":self.bid_log, "chosen_index":self.chosen_index, "client_review":self.client_review}

	#update bid_db
	def set_id(self, id):
		jsonIO.set_value(self.db, self.id, "id", id)
		self.id = id
		return 1
	def set_project_id(self, project_id):
		self.id = project_id
		return 1
	#creating bid_log
	def add_bid_log(self, bidder_id, amount, suggested_time, time = now):
		if time and bidder_id != 'Nan' and amount and suggested_time:
			(self.bid_log).append({time, bidder_id, amount, suggested_time})
			jsonIO.set_value(self.db, self.id, "bid_log", self.bid_log)
			return 1
		return 0
	def set_bid_log(self, bid_log):
		if bid_log != [[]] and bid_log and any(isinstance(bid, list) for bid in bid_log):
			if any(len(bid) != 4 for bid in bid_log):
				print(len(bid),"bid_log must contain 4 entries within another list")
				self.bid_log = [[]]
				jsonIO.set_value(self.db, self.id, "bid_log", self.bid_log)
				return 0
			else:
				self.bid_log = copy.deepcopy(bid_log) #time, bidder's id, amount, suggested end time
		else:
			self.bid_log = [[]]
		jsonIO.set_value(self.db, self.id, "bid_log", self.bid_log)
		return 1
	def set_chosen_id(self, chosen_index):
		self.chosen_index = chosen_index
		jsonIO.set_value(self.db, self.id, "chosen_index", chosen_index)
		return 1
	def set_client_review(self, client_review):
		self.client_review = client_review
		jsonIO.set_value(self.db, self.id, "client_review", client_review)
		return 1

#destructor
	def remove(self):
		jsonIO.del_row(self.db, self.id)
		print (self.id, ' was destroyed.')
		del self
		return 1