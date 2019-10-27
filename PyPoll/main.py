# Dependencies
import csv

# Files to Load
file_to_load = "Resources/election_data.csv"
file_to_output = "election_results.txt"

# Variables to Track
total_votes = 0
cantidates = {}

#select winner of election
def selectWinner(candidates):
  winner = ""
  votesWinner = 0
  for candidate in candidates:
    votes = candidates[candidate]
    if votes > votesWinner:
      votesWinner = votes
      winner = candidate
  return str(winner)

#calculate percent votes of one candidate
def calculatePercentVotes(votes):
  return round(((votes * 100.000) / total_votes),3)

def printCandidates(candidates, console, txt_file=''):
  votes = 0
  for candidate in candidates:
    votes = candidates[candidate]
    #print result of one candidate on console
    if console:
      print(candidate + ": " + str(calculatePercentVotes(votes)) + "%" + " (" + str(votes) + ")")
    #print result of one candidate on output file
    else:
      txt_file.write(candidate + ": " + str(calculatePercentVotes(votes)) + "%" + " (" + str(votes) + ")")
      txt_file.write("\n")

# Read Files
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    # Loop through all the rows of data we collect
    for row in reader:
        # Calculate the totals votes
        total_votes = total_votes + 1

        # add the votes of a candidate
        if row['Candidate'] in cantidates:
          cantidates[row['Candidate']] = cantidates[row['Candidate']] + 1
        else:
          cantidates.setdefault(row['Candidate'],1)

    # Show Output
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    printCandidates(cantidates, True)
    print("-------------------------")
    print("Winner: " + selectWinner(cantidates))

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(total_votes))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    printCandidates(cantidates, False, txt_file)
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + selectWinner(cantidates))