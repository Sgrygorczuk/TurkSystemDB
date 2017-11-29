from User import *
from Project imoport *
from Team import *
from Bid import *
from Task import *
import numpy

#for users
def calc_avg_rating(object):
	ratings = []
	if object.__class__ == Team:
		for user in object.get_dev_ids():
			for rate in user.get_ratings()
				ratings.append(rate)
	else:
		ratings = object.get_ratings()
	return max(numpy.mean(), 1)
