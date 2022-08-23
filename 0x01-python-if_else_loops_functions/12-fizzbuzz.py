#!/usr/bin/python3
def fizzbuzz():
	for i range(1,101):
		if i % 3 == 0:
			return "Fizz "
		elif i % 5 :
			return "Buzz "
		elif i % 3 == 0 and i % 5 == 0:
			return "FizzBuzz"
		else:
			return i + " "

