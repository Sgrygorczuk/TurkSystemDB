import SupportMethods as sm

class TaskDB:
	db = "taskDB"
	def __init__(self, userId = 'Nan', issueDesc = "", resolved = False):
		self.issueId = 'Nan'
		self.setAll(userId, issueDesc, resolved)
	
	#create a new DB if a new project is made by initializing class
		if self.issueId!='Nan':
			self.newIssue(userId, issueDesc, resolved)
	
	def setAll(self, userId, issueDesc, resolved):
		self.userId = userId
		self.issueDesc = issueDesc
		self.resolved = resolved #true/false
		self.getNextIssue() # get and set next unrevolved issue
	
	#will load DB into the class (must at least set ID) will return 1 or 0 upon success or failure respectively
	def loadDB(self):
		if self.issueId != 'Nan':
			self.dump(sm.loadDB(self.db,self.issueId))
			return 1
		else:
			return 0
			
	#breakdown the dictionary and load into the class
	def dump(self,dict):
		#self.issueId = dict["id"]
		self.setAll(dict["issueId"], dict["userId"], dict["issueDesc"], dict["resolved"])

	#get methods
	def getIssueId(self): 
		return self.issueId
	def getUserId(self): 
		return self.userId
	def getIssueDesc(self): 
		return self.issueDesc
	def getResolved(self): 
		return self.resolved
	def getNextIssue(self):
		self.nextIssue = sm.find(self.db, "resovled", False)
		return self.nextIssue
 
	#create a new taskDB
	def newIssue(self, userId, issueDesc, resolved): 
		self.issueId = sm.getlastId(self.db) + 1 #last+1 for new
		sm.push(self.db, self.issueId, userId, issueDesc, resolved)
		if self.userId!= userId:
			self.setAll(userId, issueDesc, resolved)
	
	#update bidDB
	def setIssueId(self, issueId):
		self.issueId = issueId
		sm.set(self.db, self.issueId, "issueId", issueId)
		return 1;
	def setUserId(self, userId):
		self.userId = userId
		sm.set(self.db, self.issueId, "userId", userId)
		return 1;
	def setIssueDesc(self, issueDesc):
		self.issueDesc = issueDesc
		sm.set(self.db, self.issueId, "issueDesc", issueDesc)
		return 1;
	def setResolved(self, resolved):
		self.resolved = resolved
		sm.set(self.db, self.issueId, "resolved", resolved)
		return 1;

	def removeTask(self):
		sm.remove(self.db, self.issueId)
		return 1;

	#destructor
	def __del__(self):
		raise Exception("Something went wrong when destroying")
		print (self.issueId, ' was destroyed.')
