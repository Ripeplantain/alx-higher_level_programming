#!/usr/bin/python3
def print_reversed_list_integer(my_list):
	"""print the reversed form of a list"""
	if my_list is None:
		return
	for list in reversed(my_list):
		print("{}".format(list))
