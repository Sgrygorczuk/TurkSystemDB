from User import *
from Project import *
from Team import *
from Bid import *
from Task import *
import ezcommands as ez
from datetime import *

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
dt_later = dt_now + timedelta(days=1)
later = dt_later.strftime("%Y-%m-%d %H:%M:%S")

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
	super_user.new_user(name = "System Admin", username = "admin", password = "pass", user_type = "admin",  balance = 100)
	user1.new_user(name = "Johnny Boy", username = "eats", password = "Dog", user_type = "developer", balance = 12)
	user2.new_user(name = "Jane Doe", username = "isa", password = 'cat', user_type = "developer", balance = 64)
	user3.new_user(name = "Cow", username = "can", password = 'code?', user_type = "developer", balance = 84)
	user4.new_user(name = "Loner", username = "Loner", password = 'in_corner', user_type = "developer", balance = 15)

	t1.new_team(admin_ids = [user1.get_id()], dev_ids = [user1.get_id(),user2.get_id()], name = "WallStreet, where many things can go wrong")
	t2.new_team(admin_ids = [user3.get_id()], dev_ids = [user3.get_id()], name = "One Cow Team")
	t3.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Rainbow Darkness")

	client1.new_user(name = "Jack Sparrow", username = "Fish", password = "cat", user_type = "client", balance = 464)
	client2.new_user(name = "Jasmin Tea", username = "is", password = 'awesome!', user_type = "client", balance = 174)
	client3.new_user(name = "Rick", username = "mr", password = 'meeseeks', user_type = "client", balance = 633)
	client4.new_user(name = "Morty", username = "rick", password = 'adventure', user_type = "client", balance = 145)

	project1.new_project(client_id = client1.get_id(), title = "Hello", desc = "I have a lot of money", bid_id = now, team_id = t1.get_id(), start_date = now, end_date = now)
	project2.new_project(client_id = client2.get_id(), title = "World", desc = "I have a lot of money, too?", bid_id = now, team_id = t2.get_id(), start_date = now, end_date = now)
	project3.new_project(client_id = client3.get_id(), title = "Goodbye", desc = "I have more money than the other guy", team_id = t3.get_id(), bid_id = now, start_date = now, end_date = now)
	project4.new_project(client_id = client4.get_id(), title = "VR", desc = "Don't listen to any of them, I have the most", bid_id = now, start_date = now, end_date = now)

	bid1.new_bid(project_id = project1.get_id(), start_date = now, end_date=now, initial_bid = 1000)
	bid2.new_bid(project_id = project2.get_id(), start_date = now, end_date=now, initial_bid = 1000)
	bid3.new_bid(project_id = project3.get_id(), start_date = now, end_date=now, initial_bid = 1000)
	bid4.new_bid(project_id = project4.get_id(), start_date = now, end_date=now, initial_bid = 1000)