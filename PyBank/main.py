
import os
import csv

# Call out path for data file
csvpath = "resources/budget_data.csv"

# Establish variables
Total_Months = 0
prev_row = 0
Date = []
Profit_Loss = []
Total_PL = 0
Change_PL = []
Avg_PL = []
Max_PL = ["", 0]
Min_PL = ["",999999999999999999]

# Establish CSV path  
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


     #Read header row 
    header = next(csvreader)
 

# Find Total Months and append to list
    for row in csvreader:
        # next(csvreader)
        Total_Months = Total_Months + 1
        Date.append(row[0])
# Append Profit loss to list; Use to determine Total PL and Net CPL    
        Profit_Loss.append(row[1])
        Total_PL += int(row[1])
        net_CPL = int(row[1])-prev_row


# Total_PL = sum (int(Profits_Losses))
    Change_List = []
    i=0
    for stats in Profit_Loss:
                 
    
        # changes in profit/loss over time period and append to list
        Change_PL = (int(stats) - prev_row)
        prev_row = (int(stats))
        Change_List.append(Change_PL)
      
    # Determine Max / min
        if Change_PL > Max_PL[1]:
            Max_PL[0] = Date[i]  
            Max_PL[1] = Change_PL

        if Change_PL< Min_PL[1]:
            Min_PL[0] = Date[i]
            Min_PL[1] = Change_PL

        i += 1
# /Determine Average profit loss   
    Change_List = Change_List[1:]
    Avg_PL = sum(Change_List)/(len(Change_List))
   
    
# Print out analysis
    print("Financial Analysis:")
    print("----------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total: ${Total_PL}")
    print(f"Average Change: ${round(Avg_PL,2)}")
    print(f"Greatest Increase in Profits: {Max_PL[0]} ({Max_PL[1]})")
    print(f"Greatest Decrease in Profits: {Min_PL[0]} ({Min_PL[1]})")

# /Establish variable for CSV write
Analysis = ("Financial Analysis:",
            "----------------------",
            (f"Total Months: {Total_Months}"),
            (f"Total: ${Total_PL}"),
            (f"Average Change: ${round(Avg_PL,2)}"),
            (f"Greatest Increase in Profits: {Max_PL[0]} ({Max_PL[1]})"),
            (f"Greatest Decrease in Profits: {Min_PL[0]} ({Min_PL[1]})"))
# # set ouput file and data to write
with open("analysis/main_edited.csv", "w") as csvfile:
    for point in Analysis:
        csvfile.write(point)
        csvfile.write('\n')
  