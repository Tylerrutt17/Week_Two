# Week two day 1 excercises // Do not or repeat yourself (DRY)

import time
#time.sleep(4)
#print("Hello Week Two!")


# Sorting Histogram
# word = input("Give me a word.\n")
# word_list = {}

# top_3 = [0, 0, 0]

# for letter in word:
#     if(letter in word_list):
#         word_list[letter] += 1
#     else:
#         word_list[letter] = 1

# for top_letter_search in word_list:
#     for index, top_letter in enumerate(top_3):
#         if word_list[top_letter_search] > top_letter[index]:
#             top_3[index] = letter

# print(top_3)

# Functions
# def my_func(initial_droid_count, destroyed_count):
#     return initial_droid_count - destroyed_count

# quote = "The ability to speak does not make you intelligent. * To Jar Jar"

# def make_quote():
#     quote = "This is not true"
#     print(quote)

# make_quote()
# print(quote)


# Mad Lib one
def mad_lib(name, subject):
    print("%s's favorite subject is %s" % (name, subject))

mad_lib("Tyler", "computer science")

# Celcius to fahrenheit
def celsius_to_fahrenheit(celsius):
    f = (celsius * 9/5) + 32
    print("%s to Fahrenheit = %s" % (celsius, f))

#celsius_to_fahrenheit(12)

# Fahrenheit to celsius
def fahrenheit_to_celcius(fahrenheit):
    c = (fahrenheit - 32) * 5/9
    print("%s to Celsius = %s" % (fahrenheit, c))

#fahrenheit_to_celcius(32)

# Even Number Check
def is_even(number):
    if (number % 2) == 0:
        return True
    else:
        return False

# Odd Number Check
def is_odd(number):
    output = is_even(number)
    if output == False:
        return True
    else:
        return False

#number_odd = is_odd(15)
#if number_odd == True:
#    print("yep its odd!")

# Only Even Numbers
def only_even(list: list):
    for counter, number in enumerate(list):
        if is_odd(number):
            del list[counter]
    
    print("Even List Numbers = %s" % list)

#only_even([21, 22, 26, 28, 2, 4])

# MEDIUM EXCERSISES

# Return lowest number
def lowest_num(list: list):
    lowest_number = float("inf")
    for num in list:
        if num < lowest_number:
            lowest_number = num
    return lowest_number

#lowest_num([1, 6, 5, 15, 22])

# Return Highest number
def highest_num(list: list):
    highest_number = float("-inf")
    for num in list:
        if num > highest_number:
            highest_number = num
    
    return highest_number

#highest_num([1, 6, 5, 15, 22])

def shortest_string(list: list):
    shortest_length = float("inf")
    shortest_string = ""
    for string in list:
        if len(string) < shortest_length:
            shortest_length = len(string)
            shortest_string = string
            
    print("The shortest string %s is %s characters long" % (shortest_string, shortest_length))
    return shortest_string

#shortest_string(["String1", "I am your father luke", "Son of Dathomir"])

def longest_string(list: list):
    longest_length = float("-inf")
    longest_string = ""
    for string in list:
        if len(string) > longest_length:
            longest_length = len(string)
            longest_string = string
            
    print("The longest string %s is %s characters long" % (longest_string, longest_length))
    return longest_string

#longest_string(["String1", "I am your father luke", "Son of Dathomir"])

# LARGE

# 1. Tic-tac-toe
# Write a function move that accepts three arguments:

# board a 2-dimensional array that represents a 3x3 tic-tac-toe board
# location a 2-item tuple that specifies an cell on the board
# player a String, either "X" or "Y"
# Return a copy of the board with the player String placed at the location.

# Throw an error if:

# The board is the wrong size
# The location is already occupied by a player
# The location is invalid
# The player String is something other than "X" or "Y"
# #2. Change maker

def move(board: [list, list, list], location: tuple, player: str):
    if len(location) > 2:
        print("Too Long!")

# You will write a function that calculates how many bills and coins someone would receive as change.

# Write a function make_change that accepts two arguments:

# total_charge - the amount of money owed
# payment - the amount of money payed
# Return a 2-dimensional tuple whose values represent the bills and coins.

# For example, consider the following tuple:

def change_maker(totalcharge: float, payment: float):
    difference = totalcharge - payment

    #if totalcharge + payment > 100
        
    