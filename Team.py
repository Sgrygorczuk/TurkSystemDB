import jsonIO

class Team:
	db = "team_db"
	
	def __init__(self, admin_ids = [], dev_ids = [], name = "", pic = "", desc = "",
		project_ids = [], active_project= "", join_request_ids = [], status = ""):
		self.id = 'Nan'
		#might call new_team later on
		self.new_team(admin_ids, dev_ids, name, pic, desc, project_ids, active_project, join_request_ids, status)

	#create a new team in db and in class
	def new_team(self, admin_ids, dev_ids, name, pic = "", desc = "", project_ids = [], active_project = 'Nan', join_request_ids = [], status = "active"):
		self.set_all(admin_ids, dev_ids, name, pic, desc, project_ids, active_project, join_request_ids, status)
		#make new class if not called explicitly
		if name:
			self.id = jsonIO.get_last_id(self.db)
			#if no ids made
			if self.id == None:
				self.id = 0
			else:
				self.id += 1 #last+1 for new
			jsonIO.add_row(self.db, self.get_all())
	
	#create a new team in class only
	def set_all(self, admin_ids, dev_ids, name, pic, desc, project_ids, active_project, join_request_ids, status, modify_db = 0):
		#should make sure array is not empty
		if admin_ids:
			self.admin_ids = list(admin_ids)					#admins are also include inside dev_ids
		else:
			self.admin_ids = []	
		if dev_ids:
			self.dev_ids = list(dev_ids)						#devs who are in the team
		else:
			self.dev_ids = []
		self.name = name
		self.pic = pic
		self.desc = desc
		if project_ids:
			self.project_ids = list(project_ids)				#project done together (will be used to find average of project done together)
		else:
			self.project_ids = []
		self.active_project = active_project					#current project being worked on
		if join_request_ids:
			self.join_request_ids = list(join_request_ids)		#join request sent by dev
		else:
			self.join_request_ids = []
		self.status = status									#active and inactive
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
		self.set_all(dict["admin_ids"], dict["dev_ids"], dict["name"], dict["pic"], dict["desc"],
		dict["project_ids"], dict["active_project"], dict["join_request_ids"], dict["status"])
		
	#get_ methods
	def get_id(self): 
		return self.id
	def get_admin_ids(self): 
		return self.admin_ids
	def get_dev_ids(self): 
		return self.dev_ids
	def get_name(self): 
		return self.name
	def get_pic(self): 
		return self.pic #one or more
	def get_desc(self): 
		return self.desc
	def get_project_ids(self):
		return self.project_ids
	def get_active_project(self):
		return self.active_project
	def get_join_request_ids(self):
		return self.join_request_ids
	def get_status(self): 
		return self.status
	def get_all(self):
		return {"id":self.id, "admin_ids":self.admin_ids, "dev_ids":self.dev_ids, "name":self.name, "pic":self.pic, "desc":self.desc,
		"project_ids":self.project_ids, "active_project":self.active_project, "join_request_ids":self.join_request_ids, "status":self.status}
	
	#update project_db
	def set_id(self, id): 
		jsonIO.set_value(self.db, self.id, "id", id)
		self.id = id
		return 1
	def add_admin_ids(self, admin_id):
		if admin_id != 'Nan':
			(self.admin_ids).append(admin_id)
			jsonIO.set_value(self.db, self.id, "admin_ids", self.admin_ids)
			return 1
		return 0
	def set_admin_ids(self, admin_ids):
		if admin_ids:
			self.admin_ids = list(admin_ids)
			jsonIO.set_value(self.db, self.id, "admin_ids", self.admin_ids)
			return 1
		return 0
	def add_dev_ids(self, dev_id):
		if dev_id != 'Nan':
			(self.dev_ids).append(dev_id)
			jsonIO.set_value(self.db, self.id, "dev_ids", self.dev_ids)
			return 1
		return 0
	def set_dev_ids(self, dev_ids):
		if dev_ids:
			self.dev_ids = list(dev_ids)
			jsonIO.set_value(self.db, self.id, "dev_ids", self.dev_ids)
			return 1
		return 0
	def set_name(self, name): 
		self.name = name
		jsonIO.set_value(self.db, self.id, "name", name)
		return 1
	def set_pic(self, pic): 
		self.pic = pic
		jsonIO.set_value(self.db, self.id, "pic", pic)
		return 1
	def set_desc(self, desc): 
		self.desc = desc
		jsonIO.set_value(self.db, self.id, "desc", desc)
		return 1
	def add_project_ids(self, project_id):
		if project_id != 'Nan':
			(self.project_ids).append(project_id)
			jsonIO.set_value(self.db, self.id, "project_ids", self.project_ids)
			return 1
		return 0
	def set_project_ids(self, project_ids):
		if project_ids:	
			self.project_ids = list(project_ids)
			jsonIO.set_value(self.db, self.id, "project_ids", self.project_ids)
			return 1
		return 0
	def set_active_project(self, active_project): 
		self.active_project = active_project
		jsonIO.set_value(self.db, self.id, "active_project", active_project)
		return 1
	def add_join_request_ids(self, join_request_id):
		if join_request_id != 'Nan':
			(self.join_request_ids).append(join_request_id)
			jsonIO.set_value(self.db, self.id, "join_request_ids", self.join_request_ids)
			return 1
		return 0
	def set_join_request_ids(self, join_request_ids):
		if join_request_ids:
			self.join_request_ids = list(join_request_ids)
			jsonIO.set_value(self.db, self.id, "join_request_ids", self.join_request_ids)
			return 1
		return 0
	def set_status(self, active_project): 
		self.active_project = active_project
		jsonIO.set_value(self.db, self.project_id, "active_project", active_project)
		return 1
		
	#destructor
	def remove(self):
		jsonIO.del_row(self.db, self.id)
		print (self.id, ' was destroyed.')
		del self
		return 1