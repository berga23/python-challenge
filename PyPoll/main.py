import os
import csv

# Path to collect data from the Resources folder
PypollCSV = os.path.join('Resources', 'election_data.csv')


# Read in the CSV file
with open(PypollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    count_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for row in csvreader:
        count_votes = count_votes + 1
        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Li":
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
    
    
    khan_percentage = khan_votes / count_votes
    correy_percentage = correy_votes / count_votes
    li_percentage = li_votes / count_votes
    otooley_percentage = otooley_votes / count_votes

    winner_percentage = max(khan_percentage, correy_percentage, li_percentage, otooley_percentage)
    
    if winner_percentage == khan_percentage:
        winner = "Khan"
    elif winner_percentage == correy_percentage:
        winner = "Correy"
    elif winner_percentage == li_percentage:
        winner = "Li"
    elif winner_percentage == otooley_percentage:
        winner = "O'Tooley"
    
    print("-----------------------------------")
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes: " + str(count_votes))
    print("-----------------------------------")
    print("Khan: " + str("{0:.0f}%".format(khan_percentage * 100)) + " (" + str(khan_votes) + ")")
    print("Correy: " + str("{0:.0f}%".format(correy_percentage * 100)) + " (" + str(correy_votes) + ")")
    print("Li: " + str("{0:.0f}%".format(li_percentage * 100)) + " (" + str(li_votes) + ")")
    print("O'Tooley: " + str("{0:.0f}%".format(otooley_percentage * 100)) + " (" + str(otooley_votes) + ")")
    print("-----------------------------------")
    print("Winner: " + str(winner))