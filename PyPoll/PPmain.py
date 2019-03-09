import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)


print("Election Results")
print(" -------------------------")
print("Total Votes:")
print(" -------------------------")
print("Khan:")
print("Correy:")
print("Li:")
print("O'Tooley:")
print("Winner:")