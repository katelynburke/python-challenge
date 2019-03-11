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
    months_profits = []
    # reader = csv.reader(bankData)
    for row in csvreader:
        total += int(row[1])
        # months_profits.append(int(row[1]))
        monthProfit = [row[0], int(row[1])]
        months_profits.append(monthProfit)

    # average of changes of profits/losses
    month_differences = []
    for idx, row in enumerate(months_profits):
        # print(row, idx) 
        # 867884 , 0
        #If the index plus 1 is less than the number of months 
        if (idx + 1) < len(months_profits):
            # 11231
            # current = months_profits[idx][1]
            # next = months_profits[idx + 1][1]
            # ['feb-2012', 12312] - ['mar-2012', 1231]
            current = months_profits[idx]
            next = months_profits[idx + 1]
            month_difference = [next[0], int(next[1] - current[1])] 
            month_differences.append(month_difference)
            # month_differences.append(int(next - current))

    # print(month_differences)

    # gives a list of all of the differences (changes) between the months
    # now, find average by adding all of the numbers in the list
    # and dividing by the length of the list
    avg_monthly_differencesTotal = 0
    for month_difference in month_differences:
        avg_monthly_differencesTotal += month_difference[1]


    print("Financial Analysis")

    print("-------------------------")

    # count the rows of data to see how many months
    # subtract the header row
    count = len(open(csvpath).readlines())
    print("Total Months:", str(count - 1))

    print(f"Total: ${str(total)}")

    avgChange = avg_monthly_differencesTotal / len(month_differences)
    print(f"Average Change: ${round(avgChange, 2)}")


    max_month = month_differences[0]
    min_month = month_differences[0]

    # ['month',difference]
    for month_difference in month_differences:
        if (month_difference[1] > max_month[1]):
            max_month = month_difference

        if (month_difference[1] < min_month[1]):
            min_month = month_difference
        
    print(f"Greatest Increase in Profits: {str(max_month[0])} (${str(max_month[1])})")
    print(f"Greatest Decrease in Profits: {str(min_month[0])} (${str(min_month[1])})")



with open('py_poll_kb.txt', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------\n")
    text.write(f"Total Months: {str(count - 1)}\n")
    text.write(f"Total: ${str(total)}\n")
    text.write(f"Average Change: ${round(avgChange, 2)}\n")
    text.write(f"Greatest Increase in Profits: {str(max_month[0])} (${str(max_month[1])})\n")
    text.write(f"Greatest Decrease in Profits: {str(min_month[0])} (${str(min_month[1])})\n")