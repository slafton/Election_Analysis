
#Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
  
    
    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vount count
        total_votes += 1

    # Print the candidate name from each row
        candidate_name = row[2]

    # If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

#Print the candidate list.
print(candidate_options)