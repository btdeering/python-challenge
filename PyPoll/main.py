import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = {}
winner = {"name": None, "votes": 0}

with open(election_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for x in csvreader:
        total_votes += 1
       
        candidate = x[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
 
        if candidates[candidate] > winner["votes"]:
            winner["name"] = candidate
            winner["votes"] = candidates[candidate]

for candidate, votes in candidates.items():
    percentage = round(votes / total_votes * 100, 3)
    candidates[candidate] = {"votes": votes, "percentage": percentage}

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in candidates.items():
    print(f"{candidate}: {data['percentage']}% ({data['votes']})")
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

output_file = os.path.join("Analysis", "election_results.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, data in candidates.items():
        txtfile.write(f"{candidate}: {data['percentage']}% ({data['votes']})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner['name']}\n")
    txtfile.write("-------------------------\n")
