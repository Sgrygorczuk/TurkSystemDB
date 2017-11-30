from User import *
from Project import *
from Team import *
from Bid import *
from Task import *
from jsonIO import *
import inspect
import numpy

##############################################################################
##############################################################################
#NOTES:
#
#Use this functions to ensure that the creation of your classes does not
#conflict with other classes, all the other classes are updated if they share
#the same key.
#This will also makes sure that there no duplicates and blacklisted
#user/project/bid... so forth are created.
#Finally this class will aid in other calculations.

##############################################################################
##############################################################################
#all classes
#get attribute from a given an instance of a class, id and key
#ex: get
def get_attribute(obj, id, key):
	return jsonIO.get_value(obj, id, key)
	
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

	#from,to,amount
def tranfer_funcs(from_user, to_user, amount):
	pass

##################################################################################
#metrics
def calc_avg_rating(object):
	ratings = []
	if object.__class__ == Team:
		for user in object.get_dev_ids():
			for rate in user.get_ratings():
				ratings.append(rate)
	else:
		ratings = object.get_ratings()
	return max(numpy.mean(), 1)
 