#!/usr/bin/env python
#title           :pyheader.py
#description     :This will create a header for a python script.
#author          :Gabriel Ionescu
#date            :2017/09/21
#notes           :only the part for project euler
#python_version  :3.6  
#==============================================================================

# Import the modules needed to run the script.
from os.path import exists
from time import strftime
import os

title = input("Enter number of the problem: ")
number = title
# Add .py to the end of the script.
title = 'problem' + title + '.py'

# Check to see if the file exists to not overwrite it.
if exists(title):
    print("\nA script with this name already exists.")
    exit(1)

descrpt = 'Problem ' + number + ' (https://projecteuler.net/)'
div = '======================================='

# Create a file that can be written to.
filename = open(title, 'w')

# Set the date automatically.
date = strftime("%Y/%m/%d")

# Write the data to the file. 
filename.write('#!/usr/bin/python')
filename.write('\n#title\t\t\t:' + title)
filename.write('\n#description\t\t:' + descrpt)
filename.write('\n#author\t\t\t:Gabriel Ionescu')
filename.write('\n#date\t\t\t:' + date)
filename.write('\n#notes\t\t\t:')
filename.write('\n#python_version\t\t:3.6')
filename.write('\n#' + div * 2 + '\n')
filename.write('\n')
filename.write('\n')

# Close the file after writing to it.
filename.close()

# Clear the screen. This line of code will not work on Windows.
os.system("cls") 
