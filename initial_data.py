from User import *
from Project import *
from Team import *
from Bid import *
from Task import *
import ezcommands as ez
from datetime import *

#run():    creates classes
#reload(): reloads the classes from db

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
dt_later = dt_now + timedelta(days=1)
later = dt_later.strftime("%Y-%m-%d %H:%M:%S")

super_user = User()
user1 = User()
user2 = User()
user3 = User()
user4 = User()

t0 = Team()
t1 = Team()
t2 = Team()
t3 = Team()

client0 = User()
client1 = User()
client2 = User()
client3 = User()
client4 = User()

project0 = Project()
project1 = Project()
project2 = Project()
project3 = Project()
project4 = Project()

bid0 = Bid()
bid1 = Bid()
bid2 = Bid()
bid3 = Bid()
bid4 = Bid()

task0 = Task()
task1 = Task()
task2 = Task()
task3 = Task()

def reload():
	super_user.load_db(0)
	user1.load_db(1)
	user2.load_db(2)
	user3.load_db(3)
	user4.load_db(4)

	t0.load_db(0)
	t1.load_db(1)
	t2.load_db(2)
	t3.load_db(3)

	client0.load_db(5)
	client1.load_db(6)
	client2.load_db(7)
	client3.load_db(8)
	client4.load_db(9)

	project0.load_db(0)
	project1.load_db(1)
	project2.load_db(2)
	project3.load_db(3)
	project4.load_db(4)

	bid0.load_db(0)
	bid1.load_db(1)
	bid2.load_db(2)
	bid3.load_db(3)
	bid4.load_db(4)
	
	task0.load_db(0)
	task1.load_db(1)
	task2.load_db(2)
	task3.load_db(3)

def run():
	super_user.new_user(name = "System Admin", username = "admin", password = "pass", user_type = "admin",  balance = 100)
	user1.new_user(name = "controlled", username = "controlled", password = "controlled", user_type = "dev", balance = 10)
	user2.new_user(name = "Jane Doe", username = "isa", password = 'cat', user_type = "dev", balance = 20, project_ids = [2], team_id = 2)
	user3.new_user(name = "Cow", username = "can", password = 'code?', user_type = "dev", balance = 30)
	user4.new_user(name = "Loner", username = "Loner", password = 'in_corner', user_type = "dev", balance = 40)

	t0.new_team(admin_ids = [user1.get_id()], dev_ids = [user1.get_id(), user2.get_id()], name = "Controlled") 
	t1.new_team(admin_ids = [user1.get_id()], dev_ids = [user1.get_id(), user2.get_id()], name = "WallStreet, where many things can go wrong")
	t2.new_team(admin_ids = [user2.get_id()], dev_ids = [user2.get_id()], name = "One Cow Team")
	t3.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Rainbow Darkness")

	client0.new_user(name = "controlled", username = "controlled", password = "controlled", user_type = "client", balance = 10, project_ids = [0])
	client1.new_user(name = "Jack Sparrow", username = "Fish", password = "cat", user_type = "client", balance = 10, project_ids = [0,1,2,3])
	client2.new_user(name = "Jasmin Tea", username = "is", password = 'awesome!', user_type = "client", balance = 20, project_ids = [2])
	client3.new_user(name = "Rick", username = "mr", password = 'meeseeks', user_type = "client", balance = 30)
	client4.new_user(name = "Morty", username = "rick", password = 'adventure', user_type = "client", balance = 40)

	project0.new_project(client_id = client0.get_id(), title = "controlled", desc = "controlled", start_date = now, end_date = later, team_id = 0)
	project1.new_project(client_id = client1.get_id(), title = "Hello", desc = "I have a lot of money", start_date = now, end_date = later, team_id = t1.get_id())
	project2.new_project(client_id = client1.get_id(), title = "World", desc = "I have a lot of money, too?", start_date = now, end_date = later, team_id = t2.get_id())
	project3.new_project(client_id = client1.get_id(), title = "Goodbye", desc = "I have more money than the other guy", start_date = now, end_date = later, team_id = t3.get_id())
	project4.new_project(client_id = client1.get_id(), title = "VR", desc = "Don't listen to any of them, I have the most", start_date = now, end_date = later, team_id = t3.get_id())

	bid0.new_bid(project_id = project1.get_id(), end_date=later, initial_bid = 10)
	bid1.new_bid(project_id = project1.get_id(), end_date=now, initial_bid = 1000)
	bid2.new_bid(project_id = project2.get_id(), end_date=now, initial_bid = 1000)
	bid3.new_bid(project_id = project3.get_id(), end_date=now, initial_bid = 1000)
	bid4.new_bid(project_id = project4.get_id(), end_date=now, initial_bid = 1000)
	
	task0.new_issue(referred_id = 1, issue_desc ="new user")
	task1.new_issue(referred_id = 2, issue_desc ="new user", admin_comment = "user denied", date_resolved = now)
	task2.new_issue(referred_id = 2, issue_desc ="new user")
	task3.new_issue(referred_id = 5, issue_desc ="quit request")