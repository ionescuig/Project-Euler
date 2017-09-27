#!/usr/bin/python
# title          :problem_19.py
# description    :Project Euler - Problem 19 (https://projecteuler.net/)
# author         :Gabriel Ionescu
# date           :2017/09/27
# version        :1.0
# notes          :
# python_version :3.6.1
# ========================================================================

"""
You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

__author__ = "Gabriel Ionescu"

def leap_years():
    # creates a list of leap years between 1901 and 2000
    
    l_years = []
    for year in range(1901,2001):
        if year % 4 == 0:
            l_years.append(year)
    return(l_years)

def main():
    leap = leap_years()
    day = 1                                 # tuesday
    total = 0
    for year in range(1901, 2001):
        for month in range(12):
            if month == 1:
                if year in leap:
                    day = (day + 29) % 7
                else:
                    day = (day + 28) % 7
            elif month in ([3,5,8,10]):
                day = (day + 30) % 7
            else:
                day = (day + 31) % 7
            if day == 6:
                total +=1
    print(total)
    
if __name__ == "__main__":
    main()