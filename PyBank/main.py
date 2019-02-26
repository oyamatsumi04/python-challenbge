#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 09:56:08 2019

@author: mbowen
"""

#imports modules and the csv file; both the .py and csv are in the same directory

import csv
import os

pybank_csv = os.path.join("PyBank.csv")

    
#opens the csv, reads the first row as the header
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    
    
    #counts the number of rows in the csv without the header    
    total_volume=sum(float(r[1]) for r in csvreader)
    
    csvfile.seek(0,0)
    month_count=sum(1 for line in csvreader)-1


    
#prints final financial analysis    
print("")
print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_volume))