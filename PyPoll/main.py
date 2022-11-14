import os
import csv

# data file path
csvpath = "Resources/election_data.csv"

# Establish variables
Total_votes = 0
ballot_ID = []
candidate = []
county = []
Stockham = 0 
DeGette = 0    
Doane = 0
#open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #read header
    header = next(csvreader)
  
    for row in csvreader:
        Total_votes = Total_votes + 1
        ballot_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

for people in candidate:

    if people == "Charles Casper Stockham":
        Stockham = Stockham + 1

    elif people == "Diana DeGette":
        DeGette = DeGette + 1

    elif people == "Raymon Anthony Doane":
        Doane = Doane + 1

# Determine percentage share of votes
Percent_Stockham = round(100 * Stockham / Total_votes, 3)
Percent_Degette = round(100 * DeGette / Total_votes, 3)
Percent_Doane = round(100 * Doane / Total_votes, 3)


#Print Anaylsis
print ("Election Results")    
print("------------------------------------------")
print(f"Total Votes: {Total_votes}")
print("------------------------------------------")  
print(f"Charles Casper Stockham: {Percent_Stockham}% ({Stockham})")
print(f"Diana DeGette: {Percent_Degette}% ({DeGette})")
print(f"Raymon Anthony Doane: {Percent_Doane}% ({Doane})")
print("------------------------------------------")

if DeGette > Stockham and DeGette > Doane:
        print("Winner: Diana DeGette")
elif Stockham > DeGette and Stockham > Doane:
        print("Winner: Charles Stockham")

elif Doane > DeGette and Doane > Stockham:
        print("Winner: Raymond Doane")

print("------------------------------------------")

# /Establish variable for CSV write
Analysis = ("Election Results",    
            "------------------------------------------",
            (f"Total Votes: {Total_votes}"),
            "------------------------------------------",  
            (f"Charles Casper Stockham: {Percent_Stockham}% ({Stockham})"),
            (f"Diana DeGette: {Percent_Degette}% ({DeGette})"),
            (f"Raymon Anthony Doane: {Percent_Doane}% ({Doane})"),
            "------------------------------------------",
            "Winner: Diana DeGette")
# # set ouput file and data to write
with open("analysis/election_data.csv", "w") as csvfile:
    for point in Analysis:
        csvfile.write(point)
        csvfile.write('\n')
  