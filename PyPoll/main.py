#import the modules
import os
import csv

#read the CSV files
csvpath = os.path.join('Resources', 'election_data.csv')

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

#The total number of votes cast
    # total = countrows

#list of candidates who received votes
    #find unique candidates

#total votes each candidate won
    #votes1 = (count Candidate "unique1")
    #votes2 = (count Candidate "unique2") ...
    #...
    
# %of votes each candidate won
    #mean(votes1/total)
    #mean(votes2/total)...

#popular vote for election
    # winner = largest count