import SupportMethods as sm

#There are UserDB>SU | Customer>Temp | Registered> Client | Developer | Blacklisted
class UserDB:
	uDB = "userDB"
	ucDB = "userCredDB"
	uiDB = "userInfoDB"
	
	def __init__(self, username = "", password = "", userType = "", status = "", balance = 0, 
		resume = "", pic = "", interest = "", issueIds = [],
		rating = 'Nan', projectIds = [], activeProject = 'Nan'):
		#userCredDB
		self.id = 'Nan'
		self.username = username
		self.password = password
		#userDB
		self.userType = userType #temp, dev, client, SU
		self.status = status #(active, blacklisted, temp)
		self.balance = balance
		#userInfoDB
		self.resume = resume
		self.interest = interest
		self.pic = pic
		self.issueIds = issueIds
		#for registered only
		self.rating = rating
		self.projectIds = projectIds #list of project Ids that has been worked or active
		self.activeProject = activeProject #a single projectId
		
		#create a new DB if a new project is made by initializing class
		if self.id!='Nan':
			self.newUser(id, username, password, userType, status, balance, resume, interest, pic, issueIds, rating, projectIds, activeProject)

	#will load DB into the class (must at least set ID) will return 1 or 0 upon success or failure respectively
	def loadDB(self):
		if self.id != 'Nan':
			self.dump(sm.loadDB(self.uDB), sm.loadDB(self.ucDB), sm.loadDB(self.uiDB))
			return 1
		else:
			return 0
	
	#breakdown the array and load into the class
	def dump(self, userDict, userCredDict, userInfoDict): 
		#self.id = dict["id"]
			self.setAll(userCredDict["username"], userCredDict["password"],
			userDict["userType"], userDict["status"], userDict["balance"],
			userInfoDict["resume"], userInfoDict["interest"], userInfoDict["pic"], userInfoDict["issueIds"],
			userInfoDict["rating"], userInfoDict["projectIds"], userInfoDict["activeProject"])
	
	#get methods user
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
	#get methods userinfo
	def getResume(self): 
		return self.resume
	def getInterest(self): 
		return self.interest
	def setIssueIds(self): 
		return self.issueIds
	#get methods for registered only
	def getprojectIds(self): 
		return self.projectIds
	def getActiveProject(self): 
		return self.activeProject
		
	#create a new userDB
	def newUser(self, id, username, password, userType, status, balance,
		resume="", pic="", interest="", issueIds = [], rating ='Nan',
		ProjectIds=[], activeProject='Nan'):
		#self.id = sm.getlastId(self.db)
		sm.push(self.ucDB, self.id, username, password)
		sm.push(self.uDB, self.id, userType, status, balance)
		sm.push(self.uiDB, self.id, resume, pic, interest, issueIds, rating, ProjectIds, activeProject)                   
		if self.id!= id:
			self.id = id
			self.setAll(username, password, userType, status, balance, resume, pic, interest, issueIds, rating, ProjectIds, activeProject)
	
	#update userDB
	def setAll(self, username, password, userType, status, balance,
		resume="", pic="", interest="", issueIds = [], rating ='Nan',
		ProjectIds=[], activeProject='Nan'):
		#userCredDB
		self.id = id
		self.username = username
		self.password = password
		#userDB
		self.userType = userType #temp, dev, client, SU
		self.status = status #(active, blacklisted, temp)
		self.balance = balance
		#userInfoDB
		self.resume = resume
		self.interest = interest
		self.pic = pic
		self.issueIds = issueIds
		#for registered only
		self.rating = rating
		self.projectIds = projectIds #list of project Ids that has been worked or active
		self.activeProject = activeProject #a single projectId
	
	#update userDB will return 1 or 0 upon success or failure respectively
	def setId(self,id):
		self.id = id		#update this class
		sm.set(self.uDB, self.id, "id", self.id) #update DB
		sm.set(self.uiDB, self.id, "id", self.id) #update DB
		sm.set(self.ucDB, self.id, "id", self.id) #update DB
		return 1			#success
	def setUserType(self, userType):
		self.userType = userType
		sm.set(self.uDB, self.id, "userType", userType)
		return 1
	def setStatus(self, status):
		self.status = status
		sm.set(self.uDB, self.id, "status", status)
		return 1
		
	#update userInfoDB
	def deposit(self, amount):
		self.amount += amount
		sm.set(self.uiDB, self.id, "balance", self.amount)
		return 1
	def withdraw(self, amount):
		if getBalance() >= amount:
			self.amount -= amount
			sm.set(self.uiDB, self.id, "balance", self.amount)
			return 1
		else:
			return 0
	
	#update userCredentialDB
	def setUsername(self, username):
		self.username = username
		sm.set(self.ucDB, self.id, "username", username)
		return 1
	def setPassword(self, password):
		self.password = password
		sm.set(self.ucDB, self.id, "password", password)
		return 1
	
	#update userInfo
	def setResume(self, resume):
		self.resume = resume
		sm.set(self.uiDB, self.id, "resume", resume)
		return 1
	def setPic(self, pic):
		self.pic = pic
		sm.set(self.uiDB, self.id, "pic", pic)
		return 1
	def setInterest(self, insterest):
		self.insterest = insterest
		sm.set(self.uiDB, self.id, "insterest", insterest)
		return 1
	def setIssueNum(self, issueNum):
		self.issueNum = issueNum
		sm.set(self.uiDB, self.id, "issueNum", issueNum)
		return 1	
	
	#update userInfoDB
	def setRating(self, rating):
		self.rating = rating
		sm.set(self.uiDB, self.id, "rating", rating)
		return 1

	#update projectDB
	def setprojectIds(self, setprojectIds):
		self.setprojectIds = setprojectIds
		sm.set(self.uiDB, self.id, "setprojectIds", setprojectIds)
		return 1
	
	def removeUser(self, id):
		sm.remove(self.ucDB, self.id)
		sm.remove(self.uDB, self.id)
		sm.remove(self.uiDB, self.id)

	#destructor
	def __del__(self):
		raise Exception("Something went wrong when destroying")
		print (self.username, ' was destroyed.')