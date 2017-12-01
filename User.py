import jsonIO

#There are _user_db>SU | Customer>Temp | Registered> Client | Developer | Blacklisted
class User:
	db = "user_db"
	
	def __init__(self, name= "", username = "", password = "", user_type = "",
		status = "", balance = 0, warning = 0, resume = "", interest = "", pic = "", issue_ids = [], team_id = 'Nan', project_ids = []):
		self.id = 'Nan'
		#might call new_user later on
		self.new_user(name, username, password, user_type, status, balance, warning, resume, interest, pic, issue_ids, team_id, project_ids)
	
	#create a new user in db and in class
	def new_user(self, name, username, password, user_type,
		status = "active", balance = 0, warning = 0, resume = "", pic = "", interest = "", issue_ids = [], team_id = 'Nan', project_ids = []):
		self.set_all(name, username, password, user_type, status, balance, warning, resume, pic, interest, issue_ids, team_id, project_ids)
		#make new class if not called explicitly
		if username:
			self.id = jsonIO.get_last_id(self.db)
			#if no ids made
			if self.id == None:
				self.id = 0
			else:
				self.id += 1 #last+1 for new
			jsonIO.add_row(self.db, self.get_all())
			
	#create a new user in class only
	def set_all(self, name, username, password, user_type,
		status, balance, warning, resume="", pic="", interest="", issue_ids = [], team_id = 'Nan', project_ids = [], modify_db = 0):
		#userCred_db
		self.name = name
		self.username = username
		self.password = password
		#user_db
		self.user_type = user_type #temp, dev, client, SU
		self.status = status #(active, blacklisted, temp)
		self.balance = balance
		self.warning = warning
		#userInfo
		self.resume = resume
		self.interest = interest
		self.pic = pic
		self.issue_ids = issue_ids
		#for registered only
		self.team_id = team_id
		self.project_ids = project_ids #list of project ids that has been worked or active
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
	
	#breakdown the array and load into the class
	def dump(self, dict):
			self.set_all(dict["name"], dict["username"], dict["password"], dict["user_type"],
			dict["status"], dict["balance"], dict["warning"], dict["resume"], dict["interest"], dict["pic"], dict["issue_ids"],
			dict["team_id"], dict["project_ids"])
	
	#get_ methods user
	def get_id(self): 
		return self.id
	def get_name(self):
		return self.name
	def get_username(self): 
		return self.username
	def get_password(self): 
		return self.password
	def get_user_type(self): 
		return self.user_type
	def get_status(self): 
		return self.status
	def get_balance(self): 
		return self.balance
	def get_warning(self):
		return self.warning
	#get_ methods userinfo
	def get_resume(self): 
		return self.resume
	def get_interest(self): 
		return self.interest
	def get_issue_ids(self): 
		return self.issue_ids
	#get_ methods for registered only
	def get_team_id(self):
		return self.team_id
	def get_project_ids(self): 
		return self.project_ids
	def get_all(self):
		return {"id":self.id, "name":self.name, "username":self.username, "password":self.password,
		"user_type":self.user_type, "status":self.status, "balance":self.balance, "warning":self.balance,
		"resume":self.resume, "pic":self.pic, "interest":self.interest, "issue_ids":self.issue_ids,
		"team_id":self.team_id, "project_ids":self.project_ids}
		
	#update user_db will return 1 or 0 upon success or failure respectively
	def set_id(self,id):
		jsonIO.set_value(self.db, self.id, "id", self.id) #update db
		self.id = id		#update this class
		return 1			#success
	def set_user_type(self, user_type):
		self.user_type = user_type
		jsonIO.set_value(self.db, self.id, "user_type", user_type)
		return 1
	def set_status(self, status):
		self.status = status
		jsonIO.set_value(self.db, self.id, "status", status)
		return 1
		
	#update userInfo_db
	def deposit(self, amount):
		self.amount += amount
		jsonIO.set_value(self.db, self.id, "balance", self.amount)
		return 1
	def withdraw(self, amount):
		if get_balance() >= amount:
			self.amount -= amount
			jsonIO.set_value(self.db, self.id, "balance", self.amount)
			return 1
		else:
			return 0
	def set_warning(self, warning):
		self.warning = warning
		jsonIO.set_value(self.db, self.id, "warning", warning)
		return 1
		
	#update userCredential_db
	def set_name(self, name):
		self.name = name
		jsonIO.set_value(self.db, self.id, "name", name)
		return 1
	def set_username(self, username):
		self.username = username
		jsonIO.set_value(self.db, self.id, "username", username)
		return 1
	def set_password(self, password):
		self.password = password
		jsonIO.set_value(self.db, self.id, "password", password)
		return 1
	
	#update userInfo
	def set_resume(self, resume):
		self.resume = resume
		jsonIO.set_value(self.db, self.id, "resume", resume)
		return 1
	def set_Pic(self, pic):
		self.pic = pic
		jsonIO.set_value(self.db, self.id, "pic", pic)
		return 1
	def set_interest(self, insterest):
		self.insterest = insterest
		jsonIO.set_value(self.db, self.id, "insterest", insterest)
		return 1
	def add_issue_ids(self, issue_id):
		set_Issue_ids(self.issue_ids.append(issue_id))
		return 1
	def set_Issue_ids(self, issue_ids):
		self.issue_ids = issue_ids[:]
		jsonIO.set_value(self.db, self.id, "issue_ids", issue_ids)
		return 1	
	
	#update userInfo_db
	def set_team_id(self, team_id):
		self.team_id = team_id
		jsonIO.set_value(self.db, self.id, "team_id", team_id)
		return 1
	def add_project_ids(self, project_id):
		set_project_ids(self.project_ids.append(project_id))
		return 1
	def set_project_ids(self, project_ids):
		self.project_ids = project_ids[:]
		jsonIO.set_value(self.db, self.id, "project_ids", project_ids)
		return 1
	
	#destructor
	def remove(self):
		jsonIO.del_row(self.db, self.self)
		print (self.id, ' was destroyed.')
		del self
		return 1