#Importing the data
import os
import csv

#Path to collect data
budget_data = os.path.join('Resources', 'budget_data.csv')

total = []
months = []
monthly_change=[]

def average (numbers):
    total = 0.0
    for number in numbers:
        total += number
    average_calculation = total/len(numbers)
    return average_calculation



# Read the file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #Remove header
    csv_header = next(csvfile)

    for row in csvreader:
        months.append(row[0])
        total.append(row[1])
        monthly_change.append(int(row[1])) 

    total_revenue = 0
    for values in total:
        total_revenue += int(values)
        
    #Print the number of months
    print(f'Total Months: {len(months)}')

    print(f'Total Profit/Losses: ${total_revenue}')

    net_change = [j-i for i,j in zip(monthly_change[:-1],monthly_change[1:])]
    print(f'Average Change ${round(average(net_change),2)}')
    

    net_change.sort(reverse=True)
    #print(net_change)
    print(f'The Greatest increase in profit: ${net_change[0]}')
    print(f'The Greatest decrease in profit:${net_change[len(net_change)-1]}')

output_path = os.path.join('Financial Analysis.txt')
with open (output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-----------------------------------------------------------------"])
    csvwriter.writerow([f'Total Months:{len(months)}'])
    csvwriter.writerow([f'Total Profit/Losses: ${total_revenue}'])
    csvwriter.writerow([f'Average Change ${round(average(net_change),2)}'])
    csvwriter.writerow([f'The Greatest increase in profit: ${net_change[0]}'])
    csvwriter.writerow([f'The Greatest decrease in profit: ${net_change[len(net_change)-1]}'])
    

