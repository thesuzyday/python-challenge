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

        rowcount=0
#total number of months (without header)
    for row in csvreader:
        rowcount = (rowcount + 1)
         print("Total months: ", rowcount)

#Total the net profit/loss
    total = sum(row[1],start=0)
    print("Total: ", total)

#Changes of Profit/Losses & Average
   #loop through data
   #row1[column1]=i
   #i=0
   #(sum i + (i+1))
   # Differences = save that somewhere...
   #loop through and then 
   # Find Mean = Differences/rowcount
 

#Greatest Increase
    #look through Differences
    #highest row = highest float
    #print (#Greatest Increase in Profits: " highestrow)

#Greatest Decrease
    #look through differences
    # lowestrow = smallest float
    #print ("Greatest Decrease in Profits: ", lowestrow)