from User import *
from Project import *
from Team import *
from Bid import *
from Task import *
import numpy

##############################################################################
##############################################################################
#NOTES:
#
#use this functions to ensure your classes are connected to essentials classes
#also to make sure no duplicates and blacklisted user/project/bid... so forth
#aren't created.

##############################################################################
##############################################################################
#all classes
#get attribute given id and keys
def get_attribute():
	pass
	
#prints table of all DB
def print_all(DB):
	pass
	
#prints all attribute of class
def print_class(object):
	pass
	
#prints a whole column of an attribute
def print_col(DB, attribute):
	pass
##############################################################################
#SU
#takes required attribute of new user and places them in SU tasks
def register_user():
	pass

#prints status of user: userType, status, warnings, and balance
def user_report():
	pass
	
##############################################################################
#for users
#will take what is required for 
def start_project():
	pass

#must have client and project id for input
#takes required feature for a bid and initiates a bid
def start_bid():
	pass	
	
def calc_avg_rating(object):
	ratings = []
	if object.__class__ == Team:
		for user in object.get_dev_ids():
			for rate in user.get_ratings():
				ratings.append(rate)
	else:
		ratings = object.get_ratings()
	return max(numpy.mean(), 1)

	#from,to,amount
def tranfer_funcs(from_user, to_user, amount):
	pass


 