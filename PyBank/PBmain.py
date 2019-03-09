# import the modules
import os
# module to read CSV files
import csv

# set the path for the file
csvpath = os.path.join("budget_data.csv")

# opened the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    # read the header row of the file
    csv_header = next(csvreader)

    # to print header
    # print(f"CSV Header: {csv_header}")

    # total begins at zero
    total = 0
    # empty list for the profits each month
    monthsProfits = []
    # reader = csv.reader(bankData)
    for row in csvreader:
        total += int(row[1])
        # monthsProfits.append(int(row[1]))
        monthProfit = [row[0], int(row[1])]
        monthsProfits.append(monthProfit)

    # average of changes of profits/losses
    monthDifferences = []
    for idx, row in enumerate(monthsProfits):
        # print(row, idx) 
        # 867884 , 0
        #If the index plus 1 is less than the number of months 
        if (idx + 1) < len(monthsProfits):
            # 11231
            # current = monthsProfits[idx][1]
            # next = monthsProfits[idx + 1][1]
            # ['feb-2012', 12312] - ['mar-2012', 1231]
            current = monthsProfits[idx]
            next = monthsProfits[idx + 1]
            monthDifference = [next[0], int(next[1] - current[1])] 
            monthDifferences.append(monthDifference)
            # monthDifferences.append(int(next - current))

    # print(monthDifferences)

    # gives a list of all of the differences (changes) between the months
    # now, find average by adding all of the numbers in the list
    # and dividing by the length of the list
    avgMonthlyDifferencesTotal = 0
    for monthDifference in monthDifferences:
        avgMonthlyDifferencesTotal += monthDifference[1]


    print("Financial Analysis")

    print("-------------------------")

    # count the rows of data to see how many months
    # subtract the header row
    count = len(open(csvpath).readlines())
    print("Total Months:", str(count - 1))

    print(f"Total: ${str(total)}")

    avgChange = avgMonthlyDifferencesTotal / len(monthDifferences)
    print(f"Average Change: ${round(avgChange, 2)}")


    max_month = monthDifferences[0]
    min_month = monthDifferences[0]

    # ['month',difference]
    for month_difference in monthDifferences:
        if (month_difference[1] > max_month[1]):
            max_month = month_difference

        if (month_difference[1] < min_month[1]):
            min_month = month_difference
        
    print(f"Greatest Increase in Profits: {str(max_month[0])} (${str(max_month[1])})")
    print(f"Greatest Decrease in Profits: {str(min_month[0])} (${str(min_month[1])})")





