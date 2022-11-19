#import the modules
import os
import csv

#read the CSV files
csvpath = os.path.join('Resources', 'budget_data.csv')

#define variables, start w zero for future adding of profit
total = 0
month = 0
previousprofit = 0
changemonth = 0
changetotal = 0
greatincmonth = ""
greatincreasechange = 0
greatdecmonth = ""
greatdecreasechange = 0

#csvreader is opening the file and pointing to first row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


#read the headers, skip (moving pointer to next row) and print
#dont need to print
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#read the rows after header
#print the 2nd row
    for row in csvreader:
        #convert to integer/currently string
        total = total + int(row[1])
        month = month + 1

        currentprofit = int(row[1]) 
        change = 0

        if previousprofit != 0:
            change = currentprofit - previousprofit 
            changemonth = changemonth + 1 
            changetotal = changetotal + change

        previousprofit = currentprofit 

        if change > greatincreasechange:
            greatincmonth = row[0]
            greatincreasechange = change

        if change < greatdecreasechange:
            greatdecmonth = row[0]
            greatdecreasechange = change


print(total)
print(month)

output = f"""
Financial Analysis
----------------------------
Total Months: {month}
Total: ${total}
Average Change: ${changetotal/changemonth:.2f}
Greatest Increase in Profits: {greatincmonth} (${greatincreasechange})
Greatest Decrease in Profits: {greatdecmonth} (${greatdecreasechange})
"""

print(output)
#use the w to write or default is read
with open("Analysis/pybank.txt", "w") as outfile:
    outfile.write(output)