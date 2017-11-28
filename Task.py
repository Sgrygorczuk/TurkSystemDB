import jsonIO

class Task_db:
	db = "task_db"
	
	def __init__(self, user_id = 'Nan', issue_desc = "", resolved = False):
		self.issue_id = 'Nan'
		#might call new_issue later on
		self.new_issue(user_id, issue_desc, resolved)
		
		#create a new task_db
	def new_issue(self, user_id, issue_desc, resolved): 
		self.issue_id = jsonIO.get_last_id(self.db) + 1 #last+1 for new
		jsonIO.add_row(self.db, self.issue_id, user_id, issue_desc, resolved)
		self.set_all(user_id, issue_desc, resolved)
		
	def set_all(self, user_id, issue_desc, resolved):
		self.user_id = user_id
		self.issue_desc = issue_desc
		self.resolved = resolved #true/false
	
	#will load db into the class (must at least set id) will return 1 or 0 upon success or failure respectively
	def load_db(self, issue_id):
		if issue_id != 'Nan':
			self.issued_id = issued_id
			self.dump(jsonIO.load_db(self.db,issue_id))
			return 1
		else:
			return 0
			
	#breakdown the dictionary and load into the class
	def dump(self,dict):
		#self.issue_id = dict["id"]
		self.set_all(dict["user_id"], dict["issue_desc"], dict["resolved"])

	#get_ methods
	def get_issue_id(self): 
		return self.issue_id
	def get_user_id(self): 
		return self.user_id
	def get_issue_desc(self): 
		return self.issue_desc
	def get_resolved(self): 
		return self.resolved
	def get_next_issue(self):
		return jsonIO.find_id(self.db, "resovled", False)
	
	#update bid_db
	def set_issue_id(self, issue_id):
		jsonIO.set_(self.db, self.issue_id, "id", issue_id)
		self.issue_id = issue_id
		return 1;
	def set_user_id(self, user_id):
		self.user_id = user_id
		jsonIO.set_(self.db, self.issue_id, "user_id", user_id)
		return 1;
	def set_issue_desc(self, issue_desc):
		self.issue_desc = issue_desc
		jsonIO.set_(self.db, self.issue_id, "issue_desc", issue_desc)
		return 1;
	def set_resolved(self, resolved):
		self.resolved = resolved
		jsonIO.set_(self.db, self.issue_id, "resolved", resolved)
		return 1;

#destructor
	def remove(self):
		jsonIO.del_row(self.db, self.task_id)
		print (self.task_id, ' was destroyed.')
		del self
		return 1;