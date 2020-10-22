# Add our dependencies.
import csv
import os
# Assign a variable for the file to load a file from a path.
file_to_load = 'Resources/election_results.csv'
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the elction results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)





# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5 The winner of the election based on popylar vote
# Import the datetime class from the datetime module.
# Print the present time.
# Close File
election_data.close()

