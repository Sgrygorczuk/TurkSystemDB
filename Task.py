import jsonIO as jio

class Task_db:
	db = "task_db"
	def __init__(self, user_id = 'Nan', issue_desc = "", resolved = False):
		self.issue_id = 'Nan'
		self.set_all(user_id, issue_desc, resolved)
	
	#create a new db if a new project is made by initializing class
		if self.issue_id!='Nan':
			self.new_issue(user_id, issue_desc, resolved)
	
	def set_all(self, user_id, issue_desc, resolved):
		self.user_id = user_id
		self.issue_desc = issue_desc
		self.resolved = resolved #true/false
		self.get_next_issue() # get_ and set_ next unrevolved issue
	
	#will load db into the class (must at least set_ ID) will return 1 or 0 upon success or failure respectively
	def load_db(self):
		if self.issue_id != 'Nan':
			self.dump(jio.load_db(self.db,self.issue_id))
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
	def get__resolved(self): 
		return self.resolved
	def get_next_issue(self):
		self.next_issue = jio.find(self.db, "resovled", False)
		return self.next_issue
 
	#create a new task_db
	def new_issue(self, user_id, issue_desc, resolved): 
		self.issue_id = jio.get_row(self.db) + 1 #last+1 for new
		jio.push(self.db, self.issue_id, user_id, issue_desc, resolved)
		if self.user_id!= user_id:
			self.set_all(user_id, issue_desc, resolved)
	
	#update bid_db
	def set_issue_id(self, issue_id):
		self.issue_id = issue_id
		jio.set_(self.db, self.issue_id, "id", issue_id)
		return 1;
	def set_user_id(self, user_id):
		self.user_id = user_id
		jio.set_(self.db, self.issue_id, "user_id", user_id)
		return 1;
	def set_issue_desc(self, issue_desc):
		self.issue_desc = issue_desc
		jio.set_(self.db, self.issue_id, "issue_desc", issue_desc)
		return 1;
	def set_resolved(self, resolved):
		self.resolved = resolved
		jio.set_(self.db, self.issue_id, "resolved", resolved)
		return 1;

	def remove_task(self):
		jio.remove(self.db, self.issue_id)
		return 1;

	#destructor
	def __del__(self):
		raise Exception("Something went wrong when destroying")
		print (self.issue_id, ' was destroyed.')
