# Dependencies
import csv

# Files to Load
file_to_load = "Resources/budget_data.csv"
file_to_output = "financial_analysis.txt"

# Variables to Track
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]
ProfitLosses = []
# Read Files
with open(file_to_load) as budget_data:
    reader = csv.DictReader(budget_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        # print(row)
        ProfitLosses.append(int(row["Profit/Losses"]))
        # Keep track of changes
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        # print(revenue_change)

        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(row["Profit/Losses"])
        # print(prev_revenue)

        # Determine the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

    revenue_changes = []
    for x in range(1, len(ProfitLosses)):
        revenue_changes.append((int(ProfitLosses[x]) - int(ProfitLosses[x-1])))

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)

    # Show Output
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(revenue_avg, 2)))
    print("Greatest Increase in Profits: " +
          str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
    print("Greatest Decrease in Profits: " +
          str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(revenue_avg, 2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " +
                   str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " +
                   str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
