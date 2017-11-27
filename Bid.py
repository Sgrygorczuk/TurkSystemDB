import SupportMethods as sm

class BidDB:
	db = "bidDB"
	def __init__(self, clientId = 'Nan' , projectId = 'Nan', startDate = 0, endDate = 0, bidLog = [[] for i in range(3)], status = "active"):
		self.bidId = 'Nan'
		self.setAll(self, clientId, projectId, startDate, endDate, bidLog, status)
		
		#create a new DB if a new project is made by initializing class
		if clientId!='Nan':
			self.newBid(clientId, projectId, startDate, endDate, bidLog, status)
	
	#will load DB into the class (must at least set ID) will return 1 or 0 upon success or failure respectively
	def loadDB(self):
		if self.bidId != 'Nan':
			self.dump(sm.loadDB(self.db,self.bidId))
			return 1
		else:
			return 0
			
	#breakdown the dictionary and load into the class
	def dump(self, dict):
		#self.bidId = dict["id"]
		self.setAll(dict["clientId"], dict["projectId"], dict["startDate"], dict["endDate"], dict["bidLog"], dict["status"])
	
	#get methods
	def getBidId(self):
		return self.bidId
	def getClientId(self):
		return self.clientId
	def getProjectId(self): 
		return self.projectId
	def getStartDate(self): 
		return self.startDate
	def getEndDate(self): 
		return self.endDate
	def getBidLog(self): 
		return self.bidLog
	def getStatus(self): 
		return self.status

	#create a new bidDB
	def newBid(self, clientId, projectId, startDate, endDate, bidLog, status):
		self.bidId = sm.getlastId(self.db)
		sm.push(self.db, self.bidId, clientId, projectId, startDate, endDate, bidLog)
		if self.clientId!= clientId:
			self.setAll(self, clientId, projectId, startDate, endDate, bidLog, status)
	
	#update bidDB
	def setAll(self, clientId, projectId, startDate, endDate, bidLog, status):
		self.clientId = clientId
		self.projectId = projectId
		self.startDate = startDate
		self.endDate = endDate
		self.bidLog = bidLog #time, bidder's id, amount
		self.status = status
	def setBidId(self, bidId):
		self.bidId = bidId
		sm.set(self.db, self.bidId, "bidId", bidId)
		return 1;
	def setClientId(self, clientId):
		self.clientId = clientId
		sm.set(self.db, self.bidId, "clientId", clientId)
		return 1;
	def setProjectId(self, projectId):
		self.projectId = projectId
		sm.set(self.db, self.bidId, "projectId", projectId)
		return 1;
	def setStartDate(self, startDate):
		self.startDate = startDate
		sm.set(self.db, self.bidId, "startDate", startDate)
		return 1;
	def setEndDate(self, endDate):
		self.endDate = endDate
		sm.set(self.db, self.bidId, "endDate", endDate)
		return 1;
	def setBidLog(self, bidLog):
		self.bidLog = bidLog[:]
		sm.set(self.db, self.bidId, "bidLog", bidLog)
		return 1;
	def setStatus(self, status):
		self.status = status
		sm.set(self.db, self.bidId, "status", status)
		return 1;

	def removeBid(self):
		sm.remove(self.db, self.bidId)
		return 1;
	
#destructor
	def __del__(self):
		raise Exception("Something went wrong when destroying")
		print (self.bidId, ' was destroyed.')