"""
Name - Week2.py
Author Name - Aashirya Kaushik
Date - 01/30/2018

"""

def squared_nums(num_list):
	"""
	Squares the numbers in num_list
	num_list: list of numbers
	Returns : List of square of the numbers from num_list
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

def restock_inventory(inventory):
	"""
	Increases inventory of each item in dictionary by 10
	inventory : a dictionary with:
		key: string that is the name of the inventory item
		value: integer that equals the number of that item currently on hand
	Returns: updated dictionary where each inventory item is restocked.

	"""
	new_dictionary = {} # create a new emply dictionary
	for key, value in inventory.items(): # look for key value pairs
		inventory[key] = value + 10 # in the inventory with the key lets say pencil increase the value by 10
	return (inventory) # returns the updated dictionary

def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: dictionary with:
		key: string that is the name of the inventory item
		value: integer that equals th number of that item currently on hand
	Returns: the same inventory_dict with any item that had 0 quantity removed.

	"""

	new_list = [] # create an empty dictionary
	for key in inventory: # iterate through the list
		if inventory[key] == 0: # check for key = 0, if it is then 
			new_list.append(key) # add it to a new list

	for keys in new_list: 
		del inventory[keys]

	return inventory

def average_grades(grades):
	"""
	Takes grades values from a dictionary ad averages them into a final grade
	grades: a dictionary of grades with:
	key: string of students name
	value: list of integer grades received in class
	Returns: dictionary that averages out the grades of each student

	"""
	
	for key, value in grades.items(): # iterate through the dictionary for key and value
		grades[key] = sum(value)/len(value) # average of the value
		
	return (grades) #return grades
