# The data we need to retrieve

# Import modules
import csv
import os

# Assign a variable for the file to load to a path
# file_to_load = 'Resources\Election_results.csv'
file_to_load = os.path.join("Resources","Election_results.csv")

# Assign a variable to SAVE the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 2. Write using open() in "w" mode

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object wtih the Reader
    file_reader = csv.reader(election_data)

    # print the header row
    headers = next(file_reader)
    print(headers)

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