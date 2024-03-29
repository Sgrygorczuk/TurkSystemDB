import jsonIO

class Issue:
	db = "issue_db"
	
	def __init__(self, referred_id = 'Nan', issue_desc = "", admin_review = "", date_resolved = "", resolved = False):
		self.id = 'Nan'
		#might call new_issue later on
		self.new_issue(referred_id, issue_desc, admin_review, date_resolved, resolved)
		
	#create a new issue in db and in class
	def new_issue(self, referred_id, issue_desc, admin_review = "", date_resolved = "", resolved = False): 
		self.set_all(referred_id, issue_desc, admin_review, date_resolved, resolved)
		#make new class if not called explicitly
		if referred_id != 'Nan':
			self.id = jsonIO.get_last_id(self.db)
			#if no ids made
			if self.id == None:
				self.id = 0
			else:
				self.id += 1 #last+1 for new
			jsonIO.add_row(self.db, self.get_all())
	
	#create a new issue in class only
	def set_all(self, referred_id, issue_desc, admin_review, date_resolved, resolved, modify_db = 0):
		self.referred_id = referred_id		# if it a new_project, ref_id = project_id
		self.issue_desc = issue_desc 		# new user, blacklisted, rating, rejected, balance, quit team, quit user
		self.admin_review = admin_review	# admin's decision and explanation
		self.date_resolved = date_resolved	# date the admin resolved this (used for blacklisted user, 1 year after)
		self.resolved = resolved 			# true/false
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
		self.set_all(dict["referred_id"], dict["issue_desc"], dict["admin_review"], dict["date_resolved"], dict["resolved"])

	#get_ methods
	def get_id(self): 
		return self.id
	def get_referred_id(self): 
		return self.referred_id
	def get_issue_desc(self): 
		return self.issue_desc
	def get_admin_review(self): 
		return self.admin_review
	def get_date_resolved(self): 
		return self.date_resolved 
	def get_resolved(self): 
		return self.resolved
	def get_next_issue(self):
		return jsonIO.find_id(self.db, "resovled", False)
	def get_all(self):
		return {"id":self.id, "referred_id":self.referred_id, "issue_desc":self.issue_desc,
		"admin_review":self.admin_review, "date_resolved":self.date_resolved, "resolved":self.resolved}
	
	#update bid_db
	def set_id(self, id):
		jsonIO.set_value(self.db, self.id, "id", id)
		self.id = id
		return 1
	def set_referred_id(self, referred_id):
		self.referred_id = referred_id
		jsonIO.set_value(self.db, self.id, "referred_id", referred_id)
		return 1
	def set_issue_desc(self, issue_desc):
		self.issue_desc = issue_desc
		jsonIO.set_value(self.db, self.id, "issue_desc", issue_desc)
		return 1
	def set_admin_review(self, admin_review):
		self.admin_review = admin_review
		jsonIO.set_value(self.db, self.id, "admin_review", admin_review)
		return 1
	def set_date_resolved(self,date_resolved):
		self.date_resolved = date_resolved
		jsonIO.set_value(self.db, self.id, "date_resolved", date_resolved)
		return 1
	def set_resolved(self, resolved):
		self.resolved = resolved
		jsonIO.set_value(self.db, self.id, "resolved", resolved)
		return 1

#destructor
	def remove(self):
		jsonIO.del_row(self.db, self.id)
		print (self.id, ' was destroyed.')
		del self
		return 1