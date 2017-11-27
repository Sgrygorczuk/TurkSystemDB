import SupportMethods as sm

#There are UserDB>SU | Customer>Temp | Registered> Client | Developer | Blacklisted
class UserDB:
	uDB = "userDB"
	ucDB = "userCredDB"
	uiDB = "userInfoDB"
	
	def __init__(self, id='Nan', username="", password="", userType="", status="", balance=0):
		self.id = id
		self.username = username
		self.password = password
		self.userType = userType #temp, dev, client, SU
		self.status = status #(active, blacklisted, temp)
		self.balance = balance
		
		#create a new DB if a new project is made by initializing class
		if self.id!='Nan':
			self.newUser(id, username, password, userType, status, balance)

	#will load DB into the class (must at least set ID) will return 1 or 0 upon success or failure respectively
	def loadDB(self):
		if self.id != 'Nan':
			self.dump(sm.loadDB(self.uDB), sm.loadDB(self.ucDB))
			return 1
		else:
			return 0
	
	#breakdown the array and load into the class
	def dump(self, userDict, userCredDict, userInfoDict): 
		#self.id = dict["id"]
			self.setAll(userDict["username"], userDict["password"], userCredDict["userType"], dict["status"], dict["balance"])
	
	#get methods
	def getId(self): 
		return self.id
	def getUsername(self): 
		return self.username
	def getPassword(self): 
		return self.password
	def getUserType(self): 
		return self.userType
	def getStatus(self): 
		return self.status
	def getBalance(self): 
		return self.balance
	
	#create a new userDB
	def newUser(self, id, username, password, userType, status, balance, resume="", pic="", interest="", issueIds = [], rating ='Nan', ProjectIds=[], activeProject='Nan'):
		#self.id = sm.getlastId(self.db)
		sm.push(self.ucDB, self.id, username, password)
		sm.push(self.uDB, self.id, userType, status, balance)
		sm.push(self.uiDB, self.id, resume, pic, interest, issueIds, rating, ProjectIds, activeProject)                   
		if self.id!= id:
			self.id = id
			self.setAll(username, password, userType, status, balance)
	
	#update userDB
	def setAll(self, username, password, userType, status, balance):
		self.id = id
		self.username = username
		self.password = password
		self.userType = userType
		self.status = status
		self.balance = balance
	
	#update userDB will return 1 or 0 upon success or failure respectively
	def setId(self,id):
		self.id = id		#update this class
		sm.set(self.uDB, self.id, "id", self.id) #update DB
		sm.set(self.uiDB, self.id, "id", self.id) #update DB
		sm.set(self.ucDB, self.id, "id", self.id) #update DB
		return 1			#success
	def setUserType(self, userType):
		self.userType = userType
		sm.set(self.uDB, self.id, "user", userType)
		return 1
	def setStatus(self, status):
		self.status = status
		sm.set(self.uDB, self.id, "user", status)
		return 1
		
	#update userInfoDB
	def deposit(self, amount):
		self.amount += amount
		sm.set(self.uiDB, self.id, "userInfoDB", self.amount)
		return 1
	def withdraw(self, amount):
		if getBalance() >= amount:
			self.amount -= amount
			sm.set(self.uiDB, self.id, "userInfoDB", self.amount)
			return 1
		else:
			return 0
	
	#update userCredentialDB
	def setUsername(self, username):
		self.username = username
		sm.set(self.ucDB, self.id, "userCredDB", username)
		return 1
	def setPassword(self, password):
		self.password = password
		sm.set(self.ucDB, self.id, "userCredDB", password)
		return 1
	def removeUser(self, id):
		sm.remove(self.ucDB, self.id)
		sm.remove(self.uDB, self.id)
		ssm.remove(self.uiDB, self.id)

	#destructor
	def __del__(self):
		raise Exception("Something went wrong when destroying")
		print (self.username, ' was destroyed.')

		
#User>SU
class SuDB(UserDB):
	def __init__(self, id=0, username="", password="", userType="", status="active", balance=0):
		UserDB.__init__(self, id, username, password, userType, status, balance)
		
#User>Customer
class CustomerDB(UserDB):
	def __init__(self, id='Nan', username="", password="", userType="", status="active", balance=0, resume="", interest="", pic="", issueIds=[]):
		UserDB.__init__(self, id, username, password, userType, status, balance)
		self.resume = resume
		self.interest = interest
		self.pic = pic
		self.issueIds = issueIds
		#create a new DB if a new project is made by initializing class
		if self.id!='Nan':
			self.newUser(id, username, password, userType, status, balance, resume, interest, pic, issueIds)
	
	#breakdown the array and load into the class
	def dump(dict): 
		#self.id = dict["id"]
		self.setAll(dict["username"], dict["password"], dict["userType"], dict["status"], dict["balance"])
	
	#get methods
	def getResume(self): 
		return self.resume
	def getInterest(self): 
		return self.interest
	def setIssueNum(self): 
		return self.issueNum
	
	#create a new userDB
	def newUser(self, id, username, password, userType, status, balance):
		#self.id = sm.getlastId(self.db)
		sm.push(self.ucDB, self.id, username, password)
		sm.push(self.uDB, self.id, userType, status, balance)
		sm.push(self.uiDB, self.id, "", "", "", "")                              ####################Needs work
		if self.id!= id:
			self.id = id
			self.setAll(username, password, userType, status, balance)
			super(B, self).
	
	#update userDB
	def setAll(self, username, password, userType, status, balance):
		self.id = id
		self.username = username
		self.password = password
		self.userType = userType
		self.status = status
		self.balance = balance
	
	#update userInfo
	def setResume(self, resume): #update JSON and this class
	def setPic(self, pic): #update JSON and this class
	def setInterest(self, insterest): #update JSON and this class
	def setIssueNum(self, issueNum): #update JSON and this class
		
		
# #User>Customer>temporary user
# class tempUser(Customer):
	# def __init__(self, username, password, balance):
	# #self, id, username, password, userType, status, balance, resume, pic, interest, issueNum
		# User.__init__(self, 'NaN', “” , username, password, “temp” , “temp” , balance, “”, “”, ‘Nan’)
		# newUser() #updates JSON database
	
	# def loadDB(id): #overload

	# #update userDB
	# def newUser(username, password, balance):
		# #places in JSON of user with temp status

		
# #User> Customer> Registered User
# class registeredUser(Customer):
	# def __init__(self, id, username, password, userType, balance, resume, pic, interest, issueNum, rating, projectIds, activeProject):
		# User.__init__(self, id, username, password, userType, “active”, balance, resume, pic, interest, issueNum)
		# self.rating = rating
		# self.projectIds = projectIds #list of project Ids that has been worked or active
		# self.activeProject = activeProject #a single projectId

	# #get methods
	# def getprojectIds(self): 
		# return self.projectIds
	# def getActiveProject(self): 
		# return self.activeProject

	# #update userInfoDB
	# def setRating(self, rating): #update JSON and this class

	# #update projectDB
	# def setprojectIds(self, setprojectIds): #update JSON and this class
	# #change activeProject by changing the projectDB (project doesn’t belong to 1 person)

	
# #User> Customer> Registered User> Client
# class client(registeredUser):
	# def __init__(self):
	# #self, id, username, password, userType, balance, resume, pic, interest, issueNum, rating, projectIds, activeProject
		# registeredUser.__init__(self, 'NaN', “”, “”, “client”, 0, “”, “”, “”, ‘Nan’, ‘Nan’, [], ‘Nan’)
	
	# def loadDB(id): #overload

	
# #User> Customer> Registered User> Developer
# class developer(registeredUser):
	# def __init__(self):
	# #self, id, username, password, userType, balance, resume, pic, interest, issueNum, rating, projectIds, activeProject
		# registeredUser.__init__(self, 'NaN', “”, “”, “developer”, 0, “”, “”, “”, ‘Nan’, ‘Nan’, [], ‘Nan’)
	
	# def loadDB(id): #overload

	
# #User> Customer> Registered User> Blacklisted User
# #User was once a registered user so inherits registered user
# class BL_user(registeredUser):
	# def __init__(self):
	# #self, id, username, password, userType, balance, resume, pic, interest, issueNum, rating, projectIds, activeProject
		# User.__init__(self, ‘Nan’, “”, “”, “”, “blacklisted”, 0,  “”, “”, “”, ‘Nan’, ‘Nan’, [], ‘Nan’)

	# def loadDB(id): #overload