'''
Python Practice for week3
Author - Aashirya Kaushik
Date - 02/11/2017
'''

def switch_case(str_list):
    '''
    Maps strings in the str_list to a new string of
    same characters, but the first letter contains
    the opposite case
    string_list: list of strings
    Returns: list of original strings, but with
    opposite casing

    '''

    word_list = []
    for word in str_list:
        word_list.append(word.swapcase())
    return word_list


def make_title(words):
    """
    Maps words in a list to words in the same list,
    but as titled strings.
    words: list of words
    Returns: new list of titled words
    """
    word_list = [] # initialize an empty list
    for word in words: #iterate over the list of words
        word_list.append(word.title()) #title case all the elements of the list and add them to a new list.
    return word_list#returns the new list.

def three_times_nums(num_list):
    """
    Maps numbers in the num_list to numbers that are
    3 times the original value
    num_list: list of numbers
    Returns: list of numbers that are of three times
    the values in num_list
    """
    new_list = [] #initialize an empty list
    for num in num_list: #iterate over the list of numbers
        new_num = num*3 #multiply all the elements of the list by 3
        new_list.append(new_num) #append to the new list
    return new_list # return the new list.


def square_nums(number_list):
    """
    Maps numbers in the number_list to numbers of
    same value, but squares the number given
    number_list: list of numbers
    Returns: list from number_list which are squared
    """
    new_list= [] #initializing an empty list
    for num in number_list: #iterating over the list
        new_number = num**2 #increasing the elements to the power of 2
        new_list.append(new_number) #add to the new list
    return new_list #return the list with squared numbers.



def double_nums(num_list):
    """
    Maps numbers in the num_list to their doubles
    num_list: list of numbers
    Returns: list of doubled numbers
    """
    numbers = []

    for num in num_list:
        new_number = num*2
        numbers.append(new_number)
    return numbers


def only_even(mixed_list):


    new_list = []
    for num in mixed_list:
        if num%2 == 0:
            new_list.append(num)
    return new_list


def test_title(names):
    """
    Filters out capitalized and non- cap words into
    their respective lists.
    names: list of names
    Returns: both lists for review
    """


def keep_lowercase(str_list):
    """
    Filters out strings that have uppercase values
    str_list: list of strings
    Returns: list of strings that do not contain
    uppercase values
    """
    new_list = []
    for element in str_list:
        if element.isuppercase:
            new_list.append(element)
    return new_list



def lessthan_5(num_list):
    """
    Filters out numbers less than five
    num_list: list of numbers
    Returns: list of numbers in the original list
    that are less than five
    """

    numbers = []
    for element in num_list:
        if element < 5:
            numbers.append(element)
    return numbers

def remove_special_characters(string_list):
    """
    Filters out strings that have non-alphanumeric
    elements
    char_list: list of strings
    Returns: list of strings that have only letters
    or numbers in them

    """
    a_list = []
    for element in string_list:
        if element == element.isalpha():
            a_list.append(element)
    return a_list


def greatest_difference(num_list):
    """
    Finds the maximum and minimum numbers in a_list
    and computes the difference.
    num_list: list of numbers
    Returns: the difference between the maximum and
    minimum numbers in num_list
    """
    new = []
    for element in num_list:
        a = max(num_list) - min(num_list)
        new.append(a)
    return new


def multiplication_total_of(num_list):
    """
    Multiplies all the numbers in num_list together
    and gives the total
    num_list: list of numbers
    Returns: the multiplied total of the numbers in
    the num_list
    """
    new_list = []
    total = 1
    for i in num_list:
        total *= i
        new_list.append(total)
    return num_list
