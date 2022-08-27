#!/usr/bin/python3

my_list = [1,2,3,4,5]

def print_list_integer(my_list=[]):
	"""Print all the integers in a list"""
	for list in my_list:
		print("{}".format(list))

print_list_integer(my_list)
