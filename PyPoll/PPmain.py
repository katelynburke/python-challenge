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
    #list of all candidate votes
    candidate_votes = []

    for vote in csvreader:
        # pulling out the candidate column
        candidate_votes.append(vote[2])

    candidate_totals = {}
    # candidate_votes is the list
    for vote in candidate_votes:
        # if IN dictionary add 1 to total
        if vote in candidate_totals:
            candidate_totals[vote] = candidate_totals[vote] + 1
        # if NOT in dictionary set = 1
        # adding the candidate to the dictionary
        else:
            candidate_totals[vote] = 1

    #print(candidate_totals)


    print("Election Results")
    print(" -------------------------")
    print("Total Votes: ", str(count - 1))
    print(" -------------------------")
    # candidate_totals = {'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}
    max_vote = 0
    max_candidate = ''
    for candidate_name, vote in candidate_totals.items():
        # need to find percentage of votes for each candidate
        # candidate votes / total votes * 100
        percentage = (vote / count) * 100
        print(f" {candidate_name}: {round(percentage, 4)}% ({str(vote)})")
        if vote > max_vote:
            max_vote = vote
            max_candidate = candidate_name

    print(" -------------------------")
    print("Winner:", max_candidate)
    print(" -------------------------")
