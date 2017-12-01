from User import *
from Project import *
from Team import *
from Bid import *
from Task import *
import ezcommands as ez
from datetime import datetime

now = str(datetime.now())

super_user = User()
user1 = User()
user2 = User()
user3 = User()
user4 = User()

t1 = Team()
t2 = Team()
t3 = Team()

client1 = User()
client2 = User()
client3 = User()
client4 = User()

project1 = Project()
project2 = Project()
project3 = Project()
project4 = Project()

bid1 = Bid()
bid2 = Bid()
bid3 = Bid()
bid4 = Bid()

def run():
	super_user.new_user(name = "System Admin", username = "admin", password = "pass", user_type = "admin")
	user1.new_user(name = "Johnny Boy", username = "eats", password = "Dog", user_type = "developer")
	user2.new_user(name = "Jane Doe", username = "isa", password = 'cat', user_type = "developer")
	user3.new_user(name = "Cow", username = "can", password = 'code?', user_type = "developer")
	user4.new_user(name = "Loner", username = "Loner", password = 'in_corner', user_type = "developer")

	t1.new_team(admin_ids = [user1.get_id()], dev_ids = [user1.get_id(),user2.get_id()], name = "WallStreet, where many things can go wrong")
	t2.new_team(admin_ids = [user3.get_id()], dev_ids = [user3.get_id()], name = "One Cow Team")
	t3.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Rainbow Darkness")

	client1.new_user(name = "Jack Sparrow", username = "Fish", password = "cat", user_type = "client")
	client2.new_user(name = "Jasmin Tea", username = "is", password = 'awesome!', user_type = "client")
	client3.new_user(name = "Rick", username = "mr", password = 'meeseeks', user_type = "client")
	client4.new_user(name = "Morty", username = "rick", password = 'adventure', user_type = "client")

	project1.new_project(client_id = client1.get_id(), title = "Hello", desc = "I have a lot of money", bid_id = now, team_id = t1.get_id(), start_date = now, end_date = now)
	project2.new_project(client_id = client2.get_id(), title = "World", desc = "I have a lot of money, too?", bid_id = now, team_id = t2.get_id(), start_date = now, end_date = now)
	project3.new_project(client_id = client3.get_id(), title = "Goodbye", desc = "I have more money than the other guy", team_id = t3.get_id(), bid_id = now, start_date = now, end_date = now)
	project4.new_project(client_id = client4.get_id(), title = "VR", desc = "Don't listen to any of them, I have the most", bid_id = now, start_date = now, end_date = now)

	bid1.new_bid(project_id = project1.get_id(), start_date = now, end_date=now)
	bid2.new_bid(project_id = project2.get_id(), start_date = now, end_date=now)
	bid3.new_bid(project_id = project3.get_id(), start_date = now, end_date=now)
	bid4.new_bid(project_id = project4.get_id(), start_date = now, end_date=now)