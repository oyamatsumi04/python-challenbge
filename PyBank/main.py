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


#creates the function 
def financial_analysis(financial_data):
    total_volume=0.
    for volume in financial_data:
        total_volume+=int(financial_data[1])
    
    
#opens the csv, reads the first row as the header
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    
    
#counts the number of rows in the csv without the header    
    month_count=sum(1 for line in csvfile)
    
    
#retreives data from the csv
    for rows in csvreader:
        financial_analysis(rows)


#prints final financial analysis    
print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_volume))
    