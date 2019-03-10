import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    csv_header = next(csvreader)

# total number of votes cast
# number of rows minus header
    count = len(open(csvpath).readlines())

# empty dictionary

    frequency = {}

    for candidate_name in votes:
        count = frequency.get(word, 1)
        frequency[candidate_name] = count + 1
    
    frequency_list = frequency.keys()

    for words in frequency_list:
        print(words, frequency[words])

   # total = 0
    # winnerVotes = []
    # for row in csvreader:
       # total += str(row[2])
       # winnerVote = (row [0])
        # winnerVotes.append(winnerVote)

    # max_votes = winnerVotes[0]

   # for winnerVote in winnerVotes:
       # if (winnerVote[0] > max_votes[0]):
           # max_votes = winnerVote

  # print(max_votes)

    # loop through the candidates and count them - index 2


print("Election Results")
print(" -------------------------")
print("Total Votes: ", str(count - 1))
print(" -------------------------")
print("Khan:")
print("Correy:")
print("Li:")
print("O'Tooley:")
print(" -------------------------")
print("Winner:")
print(" -------------------------")