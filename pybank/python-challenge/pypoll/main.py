import os
import csv

election_data_csv = os.path.join("./Resources/election_data.csv")

total_votes = 0

total_candidates = 0

candidate_votes = 0

candidate_1_votes = 0

candidate_2_votes = 0

candidate_3_votes = 0







with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader) 

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")
        
  




print("Election Results")
print("---------------------------------")

print("Total Votes: " + str(total_votes))
print("----------------------------------")

