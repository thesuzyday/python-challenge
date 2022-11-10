#import the modules
import os
import csv

#read the CSV files
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

#read the headers, skip and print
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#read the rows after header
    for row in csvreader:
        print(row)

#Total the net profit/loss
    sum(row[1],start=0)
    

