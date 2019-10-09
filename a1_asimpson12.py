#!/usr/bin/env python3
'''
OPS435 Assignment 1 - Fall 2019
Program: a1_asimpson12.py
Author: Andre Simpson
The python code in this file (a1_asimpson12.py) is original work written by
Andre Simpson. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''

#Import required modules
import os
import sys

def usage():
    '''Prints syntax of command line arguments for script (shown when invalid arguments are supplied)'''
    print("Usage: a1_rchan.py [--step] YYYY/MM/DD +/-n")

def leap_year(year):
    '''Returns the number of days in February of a given year'''
    if year % 4 == 0:
        return 29
    else:
        return 28

def days_in_month(year):
    '''Returns a list of the lengths of each month of a given year'''
    return [0, 31, leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def valid_date(given_date):
    '''
    Returns True if the date supplied is in the format yyyy/mm/dd containing only integers and /,
    the year is past 1582, the month is between 1 and 12, and the amount
    of days specified isn't greater than the length of the given month
    '''
    if len(set(given_date) - {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "/"}) != 0:
        return False
    if len(given_date) != 10:
        return False
    if given_date[4] != '/' or given_date[7] != '/':
        return False
    if int(given_date[5:7]) < 1 or int(given_date[5:7]) > 12:
        return False
    if int(given_date[8:]) > days_in_month(int(given_date[0:4]))[int(given_date[5:7])]: #if the day value of given date is greater than the entry [month] in list days_in_month[year], false
        return False
    if int(given_date[0:4]) < 1582: #Gregorian Calendar was made official by the Vatican in 1582, spawning its adoption throughout Europe.  Using this date as init of our calendar system.  
        return False
    return True

def after(given_date):
    '''Increments the given date by one day, and returns it in yyyy/mm/dd format as a string'''
    last_day = int(days_in_month(int(given_date[0:4]))[int(given_date[5:7])])
    if int(given_date[8:]) == last_day:
        new_date = given_date[0:5] + str(int(given_date[5:7]) + 1) + "/01"
        if new_date[5:7] == "13":
            new_date = str(int(given_date[0:4]) + 1) + "/01/01"
    else:
        new_date = given_date[0:8] + str(int(given_date[8:]) + 1)
    return new_date
 

    


#=====================Handle Arguments=============================

#Check for proper number of arguments, print usage msg if improper
if len(sys.argv) < 3:
    usage()
    exit()
if sys.argv[1] == "--step" and len(sys.argv) < 4:
    usage()
    exit()

#Check for --step argument, store input as appropriate
if len(sys.argv) == 4 and sys.argv[1] == "--step":
    step = True
    user_date = sys.argv[2]
    amt_to_change = sys.argv[3]
else:
    step = False
    user_date = sys.argv[1]
    amt_to_change = sys.argv[2]

#Store user input
#user_date = sys.argv[1]
#amt_to_change = sys.argv[2]

#Alias date string ranges for code readability
y = user_date[0:4]
m = user_date[5:7]
d = user_date[8:]

#===========================Test Prints========================
#print("year: " + y)
#print("month: " + m)
#print("day: " + d)

#print(days_in_month(int(y)))
#print(valid_date(user_date))
print(after(user_date))
