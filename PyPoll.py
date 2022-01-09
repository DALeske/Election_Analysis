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

# 1. The total number of votes cast
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in then CSV file
    for row in file_reader:
        # Add to the total vote  count
        total_votes += 1  # alternate total_votes = total_votes + 1

# 2. A complete list of candidates who received votes
        # Print candidate name from each row
        candidate_name = row[2]

        # Add candidate name to the list if it is not in the list of candidate options
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Start Tracking votes
            candidate_votes[candidate_name] = 0

        # Add votes to each candidate
        candidate_votes[candidate_name] += 1
# save the results to a text file
with open(file_to_save,"w") as txt_file:
    election_results = (f"\nElection Results\n"
    f"--------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"--------------------------\n")
    print(election_results, end="")
    # save the final vote countot the text file.
    txt_file.write(election_results)

    # 3. The total nuumber of votes each candidate won
    # Find percantage of votes and print
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
    # 4. The percentage of votes each candidate won
        vote_percentage = float(votes) / float(total_votes)*100
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}) of the total vote\n")
        #print each candidate and their results to text file
        print(candidate_results)
        # Save the candidate results to the text file
        txt_file.write(candidate_results)
    
    # 5. The winner of the election base on popular vote
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
    txt_file.write(winning_candidate_summary)










