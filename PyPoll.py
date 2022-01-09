# The data we need to retrieve

# Import modules
import csv
import os

# Assign a variable for the file to load to a path
# file_to_load = 'Resources\Election_results.csv'
file_to_load = os.path.join("Resources","Election_results.csv")

# Assign a variable to SAVE the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter (and set to 0)
total_votes = 0
# Declare candidate list
candidate_options = []
# Declare Vot Count Dictionary
candidate_votes = {}
# Winning Candidae and Winning Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in then CSV file
    for row in file_reader:
        # Add to the total vote  count
        total_votes += 1  # alternate total_votes = total_votes + 1

        # Print candidate name from each row
        candidate_name = row[2]

        # Add candidate name to the list if it is not in the list of candidate options
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Start Tracking votes
            candidate_votes[candidate_name] = 0

        # Add votes to each candidate
        candidate_votes[candidate_name] += 1

# Print total Votes
#print(total_votes)

#Print the candidate list
#print(candidate_options)

# Print Candidate Votes
#print(candidate_votes)

# Find percantage of votes and print
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes)*100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}) of the total vote ({total_votes})\n")

    # Determine winning count and percentage
    if votes > winning_count and vote_percentage > winning_percentage:
        winning_count = votes
        winning_percentage = vote_percentage
        # Determine Winniing name
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count:,}\n"
    f"WInning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------\n")
print(winning_candidate_summary)

# To do: perform analysis


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The total nuumber of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election base on popular vote






# Write the data
# use the open statement to open the file as a text file
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")