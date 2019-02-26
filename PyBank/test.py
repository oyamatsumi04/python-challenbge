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


def change(last_month, current_month):
    return (float(current_month) - float(last_month))

#opens the csv, reads the first row as the header
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    
    for eachRow in csvreader:
        monthly_differences=change((csvfile[1,1])
        
        print(monthly_differences)
    


    