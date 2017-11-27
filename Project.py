import SupportMethods as sm

class ProjectDB:
	db = "projectDB"
	
	def __init__(self, clientId='Nan', bidId='Nan', devIds=[], title="", desc="", startDate=0, endDate=0, status="active"):
		self.projectId = 'Nan'
		self.setAll(clientId, bidId, devIds, title, desc, startDate, endDate, status)
		
		#create a new DB if a new project is made by initializing class
		if clientId!='Nan':
			self.newProject(clientId, bidId, devIds, title, desc, startDate, endDate, status)

	#will load DB into the class (must at least set ID) will return 1 or 0 upon success or failure respectively
	def loadDB(self):
		if self.projectId != 'Nan':
			self.dump(sm.loadDB(self.db,self.projectId))
			return 1
		else:
			return 0

	#breakdown the dictionary and load into the class
	def dump(self,dict):
		#self.projectId = dict["id"]
		self.setAll(dict["clientId"], dict["bidId"], dict["devIds"], dict["title"],dict["desc"], dict["startDate"], dict["endDate"], dict["status"])
		
	#get methods
	def getProjectId(self): 
		return self.projectId
	def getClientId(self): 
		return self.clientId
	def getBidId(self): 
		return self.bidId
	def getDevIds(self): 
		return self.devIds #one or more
	def getTitle(self): 
		return self.title
	def getDesc(self): 
		return self.desc
	def startDate(self):
		return self.startDate
	def getEndDate(self): 
		return self.endDate
	def getStatus(self): 
		return self.status

	#create a new projectDB
	def newProject(self, clientId, bidId, devIds, title, desc, startDate, endDate, status):
		self.projectId = sm.getlastId(self.db) + 1 #last+1 for new
		sm.push(self.db, self.projectId, clientId, bidId, devIds, title, desc, startDate, endDate, status)
		if self.clientId!= clientId:
			self.setAll(clientId, bidId, devIds, title, desc, startDate, endDate, status)
	
	#update projectDB
	def setAll(self, clientId, bidId, devIds, title, desc, startDate, endDate, status):
		self.clientId = clientId
		self.bidId = bidId
		self.devIds = devIds
		self.title = title
		self.desc = desc
		self.startDate = startDate
		self.endDate = endDate
		self.status = status
	def setClientId(self, clientId):
		self.clientId = clientId
		sm.set(self.db, self.projectId, "clientId", clientId)
		return 1;
	def setBidId(self, bidId):
		self.bidId = bidId
		sm.set(self.db, self.projectId, "bidId", bidId)
		return 1;
	def setDevIds(self, devIds):
		self.devIds = devIds[:]
		sm.set(self.db, self.projectId, "devIds", devIds)
		return 1;
	def setTitle(self, title):
		self.title = title
		sm.set(self.db, self.projectId, "title", title)
		return 1;
	def setDesc(self, desc):
		self.desc = desc
		sm.set(self.db, self.projectId, "desc", desc)
		return 1;
	def setStartDate(self, startDate):
		self.startDate = startDate
		sm.set(self.db, self.projectId, "startDate", startDate)
		return 1;
	def setEndDate(self, endDate):
		self.endDate = endDate
		sm.set(self.db, self.projectId, "endDate", endDate)
		return 1;
	def setStatus(self, status):
		self.status = status
		sm.set(self.db, self.projectId, "status", status)
		return 1;
		
	def removeProject(self):
		sm.remove(self.db, self.projectId)
		return 1;

	#destructor
	def __del__(self):
		raise Exception("Something went wrong when destroying")
		print (self.projectId, ' was destroyed.')
