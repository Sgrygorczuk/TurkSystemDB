import jsonIO

class Team:
	db = "team_db"
	
	def __init__(self, admin_ids = [], dev_ids = [], name = "", pic = "", desc = "", project_ids = [], active_project= "", status = ""):
		self.id = 'Nan'
		#might call new_team later on
		self.new_team(admin_ids, dev_ids, name, pic, desc, project_ids, active_project, status)

	#create a new team in db and in class
	def new_team(self, admin_ids, dev_ids, name, pic, desc, project_ids, active_project, status):
		self.id = jsonIO.get_last_id(self.db) + 1 #last+1 for new
		jsonIO.add_row(self.db, self.id, admin_ids, dev_ids, name, pic, desc, project_ids, active_project, status)
		self.set_all(admin_ids, dev_ids, name, pic, desc, project_ids, active_project, status)
	
	#create a new team in class only
	def set_all(self, admin_ids, dev_ids, name, pic, desc, project_ids, active_project, status):
		self.admin_ids = admin_ids
		self.dev_ids = dev_ids
		self.name = name
		self.pic = pic
		self.project_ids = project_ids
		self.active_project = active_project
		self.status = status
		
	#will load db into the class (must at least set id) will return 1 or 0 upon success or failure respectively
	def load_db(self, id):
		if id != 'Nan':
			self.id = id
			self.dump(jsonIO.get_row(self.db, id))
			return 1
		else:
			return 0

	#breakdown the dictionary and load into the class
	def dump(self,dict):
		#self.project_id = dict["id"]
		self.set_all(dict["admin_ids"], dict["dev_ids"], dict["name"], dict["pic"], dict["desc"], dict["project_ids"], dict["active_project"], dict["status"])
		
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
	def get_status(self): 
		return self.status

	#update project_db
	def set_id(self, id): 
		jsonIO.set_row(self.db, self.id, "id", id)
		self.id = id
		return 1;
	def set_admin_ids(self, admin_ids): 
		self.admin_ids = admin_ids
		jsonIO.set_row(self.db, self.id, "admin_ids", admin_ids)
		return 1;
	def get_dev_ids(self, dev_ids): 
		self.dev_ids = dev_ids
		jsonIO.set_row(self.db, self.id, "dev_ids", dev_ids)
		return 1;
	def get_name(self, name): 
		self.name = name
		jsonIO.set_row(self.db, self.id, "name", name)
		return 1;
	def get_pic(self, pic): 
		self.pic = pic
		jsonIO.set_row(self.db, self.id, "pic", pic)
		return 1;
	def get_desc(self, desc): 
		self.desc = desc
		jsonIO.set_row(self.db, self.id, "desc", desc)
		return 1;
	def get_project_ids(self, project_ids):
		self.project_ids = project_ids
		jsonIO.set_row(self.db, self.id, "project_ids", project_ids)
		return 1;
	def get_active_project(self, active_project): 
		self.active_project = active_project
		jsonIO.set_row(self.db, self.id, "active_project", active_project)
		return 1;
	def get_status(self, active_project): 
		self.active_project = active_project
		jsonIO.set_row(self.db, self.project_id, "active_project", active_project)
		return 1;
		
	#destructor
	def remove(self):
		jsonIO.del_row(self.db, self.id)
		print (self.id, ' was destroyed.')
		del self
		return 1;