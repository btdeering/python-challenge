import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

total_months = 0
net_total = 0
previous_month_profit = None
changes = []
greatest_increase = {"date": None, "amount": 0}
greatest_decrease = {"date": None, "amount": 0}

with open(budget_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        if previous_month_profit is not None:
            change = int(row[1]) - previous_month_profit
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = row[0]
                
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = row[0]
                
        previous_month_profit = int(row[1])

average_change = sum(changes) / len(changes)

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

output_file = os.path.join("Analysis", "financial_analysis.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")
