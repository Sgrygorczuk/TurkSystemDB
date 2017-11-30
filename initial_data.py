from User import *
from Project import *
from Team import *
from Bid import *
from Task import *
import ezcommands
from datetime import datetime


now = str(datetime.now())

super_user = User(name = "System Admin", username = "admin", password = "pass", user_type = "admin")
user1 = User(name = "Johnny Boy", username = "eats", password = "Dog", user_type = "developer")
user2 = User(name = "Jane Doe", username = "isa", password = 'cat', user_type = "developer")
user3 = User(name = "Cow", username = "can", password = 'code?', user_type = "developer")
user4 = User(name = "Loner", username = "Loner", password = 'in_corner', user_type = "developer")

t1 = Team(admin_ids = [user1.get_id()], dev_ids = [user1.get_id(),user2.get_id()], name = "WallStreet, where many things can go wrong")
t2 = Team(admin_ids = [user3.get_id()], dev_ids = [user3.get_id()], name = "One Cow Team")
t3 = Team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Rainbow Darkness")

client1 = User(name = "Jack Sparrow", username = "Fish", password = "cat", user_type = "client")
client2 = User(name = "Jasmin Tea", username = "is", password = 'awesome!', user_type = "client")
client3 = User(name = "Rick", username = "mr", password = 'meeseeks', user_type = "client")
client4 = User(name = "Morty", username = "rick", password = 'adventure', user_type = "client")

project1 = Project(client_id = client1.get_id(), title = "Hello", desc = "I have a lot of money", bid_id = now, team_id = t1.get_id(), start_date = now, end_date = now)
project2 = Project(client_id = client2.get_id(), title = "World", desc = "I have a lot of money, too?", bid_id = now, team_id = t2.get_id(), start_date = now, end_date = now)
project3 = Project(client_id = client3.get_id(), title = "Goodbye", desc = "I have more money than the other guy", team_id = t3.get_id(), bid_id = now, start_date = now, end_date = now)
project4 = Project(client_id = client4.get_id(), title = "VR", desc = "Don't listen to any of them, I have the most", bid_id = now, start_date = now, end_date = now)

bid1 = Bid(client_id = client1.get_id(),project_id = project1.get_id(), start_date = now, end_date=now)
bid2 = Bid(client_id = client2.get_id(),project_id = project2.get_id(), start_date = now, end_date=now)
bid3 = Bid(client_id = client3.get_id(),project_id = project3.get_id(), start_date = now, end_date=now)
bid4 = Bid(client_id = client4.get_id(),project_id = project4.get_id(), start_date = now, end_date=now)