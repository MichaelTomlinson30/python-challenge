import os
import csv

budget_data_csv = os.path.join("./Resources/budget_data.csv")

month_count = 0
greatest_increase = 0
greatest_decrease = 0
best_month = ''
worst_month = ''
average_change = ''
total_profit_loss = 0



change = []
month_to_month = []


with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader) 

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

    first_row = next(csvreader)
    total_profit_loss += int(first_row[1])
    previous_total_profit_loss = int(first_row[1])
    month_count += 1
    
    for row in csvreader:
      month_count += 1
      current_profit = int(row[1])
      total_profit_loss += (current_profit)
      net_change = (current_profit) - (previous_total_profit_loss)
      previous_total_profit_loss = current_profit
      change.append(net_change)

      if net_change > greatest_increase:
       best_month = (row[0])
       greatest_increase = net_change
      elif net_change < greatest_decrease:
       worst_month = (row[0])
       greatest_decrease = net_change
             
     


print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(sum(change) / len(change)))
print("Greatest Increase in Profits: " + str(best_month) + "  ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(worst_month) + "  ($" + str(greatest_decrease) + ")")

with open('Financial_Summary.txt', 'w') as f:

 f.write("Financial Analysis")
 f.write("-------------------")
 f.write("Total Months: " + str(month_count))
 f.write("Total: $" + str(total_profit_loss))
 f.write("Average Change: $" + str(sum(change) / len(change)))
 f.write("Greatest Increase in Profits: " + str(best_month) + "  ($" + str(greatest_increase) + ")")
 f.write("Greatest Decrease in Profits: " + str(worst_month) + "  ($" + str(greatest_decrease) + ")")
