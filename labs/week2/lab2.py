"""
Name - Week2.py
Author Name - Aashirya Kaushik
Date - 01/30/2018

"""
def squared_nums(num_list):
	"""
	Squares the numbers in num_list
	num_list: list of numbers
	Returns : List of square of the numbers from 
	"""
	new_list = [] # initialize a new list
	for num in num_list: # iterate through the list
		squared_num = pow(num, 2) # raises to the power of 2
		new_list.append(squared_num) # appends the result to the new list
	return new_list # returns the new list

