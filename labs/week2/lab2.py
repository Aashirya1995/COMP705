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

def check_title(title_list):
	"""
	Removes strings in title_list that have numbers and are not title case
	title_list = list of strings
	Returns: list of strings that are titles

	"""
	new_list = [] #Initialize a new list
	for title in title_list: # iterates through the list to look for the non-titles
		if title.istitle(): # checks for titles
			new_list.append(title) # if found, appends to the new list
	return new_list # returns the new appended list.
