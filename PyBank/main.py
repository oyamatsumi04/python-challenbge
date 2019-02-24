#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 09:56:08 2019

@author: mbowen
"""

#imports the csv file; both the .py and csv are in the same directory
import csv
import os

pybank_csv = os.path.join("PyBank.csv")

    
#opens the csv, reads the first row as the header
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
 
    #sums all values in column 2
    total_volume=sum(float(r[1]) for r in csvreader)
    
    #resets the for loop location to the top row
    csvfile.seek(0)
    
    #counts the number of rows in the csv without the header    
    month_count=(sum(1 for line in csvreader))-1
    
#prints final financial analysis    
print("")
print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_volume))

    