#Importing the data
import os
import csv
import statistics

election_df = "election_data.csv"
candidate_list = []

# Read file 
with open(election_df) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    print(f'Names of Candidates:{candidate_list}')

    with open(election_df) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvfile)
        khan_votes = 0 
        correy_votes = 0
        li_votes = 0
        otooley_votes = 0


#looping through the data
        for row in csvreader:
            if row[2] == "Khan":
                khan_votes += 1
            elif row[2] == "Correy":
                correy_votes +=1
            elif row[2] == "Li":
                li_votes +=1
            elif row[2] == "O'Tooley":
                otooley_votes += 1
total_votes = khan_votes + correy_votes + li_votes + otooley_votes
print("Election Results")
print("-------------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------------------------------")
print(f'Khan: {round((khan_votes/total_votes)*100,3)}%)({khan_votes})')
print(f'Correy: {round((correy_votes/total_votes)*100,3)}%)({correy_votes})')
print(f'Li: {round((li_votes/total_votes)*100,3)}%)({li_votes})')
print(f'OTooley: {round((otooley_votes/total_votes)*100,3)}%)({otooley_votes})')
print("-------------------------------------------------------")

if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes and khan_votes:
    winner = "Khan"
    print("Winner: Khan")
elif correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes and correy_votes:
    winner = "Correy"
    print("Winenr: Correy")
elif li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes and li_votes:
    winner = "Li"
    print("Winner: Li")
elif otooley_votes> khan_votes and otooley_votes > correy_votes and otooley_votes > li_votes and otooley_votes:
    winner:"OTooley"
    print("Winner: OTooley")

output_path = os.path.join('Election Results.txt')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f'Total Votes: {total_votes}'])
    csvwriter.writerow(["-------------------------------------------------------"])
    csvwriter.writerow([f'Khan: {round((khan_votes/total_votes)*100,3)}%)({khan_votes})'])
    csvwriter.writerow([f'Correy: {round((correy_votes/total_votes)*100,3)}%)({correy_votes})'])
    csvwriter.writerow([f'Li: {round((li_votes/total_votes)*100,3)}%)({li_votes})'])
    csvwriter.writerow([f'OTooley: {round((otooley_votes/total_votes)*100,3)}%)({otooley_votes})'])
    csvwriter.writerow(["--------------------------------------------------------"])
    csvwriter.writerow([f'Winner:{winner}'])




    
