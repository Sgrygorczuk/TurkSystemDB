from User import *
from Project import *
from Team import *
from Bid import *
from Issue import *
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

team0 = Team()
team1 = Team()
team2 = Team()
team3 = Team()

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

issue0 = Issue()
issue1 = Issue()
issue2 = Issue()
issue3 = Issue()

def reload():
	super_user.load_db(0)
	user1.load_db(1)
	user2.load_db(2)
	user3.load_db(3)
	user4.load_db(4)

	team0.load_db(0)
	team1.load_db(1)
	team2.load_db(2)
	team3.load_db(3)

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
	
	issue0.load_db(0)
	issue1.load_db(1)
	issue2.load_db(2)
	issue3.load_db(3)

def run():
	super_user.new_user(name = "System Admin", username = "admin", password = "pass", user_type = "admin",  balance = 100)
	user1.new_user(name = "controlled", username = "controlled", password = "controlled", user_type = "dev", balance = 10)
	user2.new_user(name = "Jane Doe", username = "isa", password = 'cat', user_type = "dev", balance = 20, project_ids = [2], team_id = 2)
	user3.new_user(name = "Cow", username = "can", password = 'code?', user_type = "dev", balance = 30)
	user4.new_user(name = "Loner", username = "Loner", password = 'in_corner', user_type = "dev", balance = 40)

	team0.new_team(admin_ids = [user1.get_id()], dev_ids = [user1.get_id(), user2.get_id()], name = "Controlled") 
	team1.new_team(admin_ids = [user1.get_id()], dev_ids = [user1.get_id(), user2.get_id()], name = "WallStreet, where many things can go wrong")
	team2.new_team(admin_ids = [user2.get_id()], dev_ids = [user2.get_id()], name = "One Cow Team")
	team3.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Rainbow Darkness")

	client0.new_user(name = "controlled", username = "controlled", password = "controlled", user_type = "client", balance = 10, project_ids = [0])
	client1.new_user(name = "Jack Sparrow", username = "Fish", password = "cat", user_type = "client", balance = 10, project_ids = [0,1,2,3])
	client2.new_user(name = "Jasmin Tea", username = "is", password = 'awesome!', user_type = "client", balance = 20, project_ids = [2])
	client3.new_user(name = "Rick", username = "mr", password = 'meeseeks', user_type = "client", balance = 30)
	client4.new_user(name = "Morty", username = "rick", password = 'adventure', user_type = "client", balance = 40)

	project0.new_project(client_id = client0.get_id(), title = "controlled", desc = "controlled",  deadline = later, team_id = 0)
	project1.new_project(client_id = client1.get_id(), title = "Hello", desc = "I have a lot of money",  deadline = later, team_id = team1.get_id())
	project2.new_project(client_id = client1.get_id(), title = "World", desc = "I have a lot of money, too?", deadline = later, team_id = team2.get_id())
	project3.new_project(client_id = client1.get_id(), title = "Goodbye", desc = "I have more money than the other guy", deadline = later, team_id = team3.get_id())
	project4.new_project(client_id = client1.get_id(), title = "VR", desc = "Don't listen to any of them, I have the most", deadline = later, team_id = team3.get_id())

	bid0.new_bid(project_id = project1.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	bid1.new_bid(project_id = project1.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	bid2.new_bid(project_id = project2.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	bid3.new_bid(project_id = project3.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	bid4.new_bid(project_id = project4.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	
	issue0.new_issue(referred_id = 1, issue_desc ="new user")
	issue1.new_issue(referred_id = 2, issue_desc ="new user", admin_review = "user denied", date_resolved = now)
	issue2.new_issue(referred_id = 2, issue_desc ="new user")
	issue3.new_issue(referred_id = 5, issue_desc ="quit request")