from file_class import FileClass
from calculator_class import CalculatorClass

file_name = "./pyBank/data/budget_data.csv"
fileExport = "./pyBank/data/budget_data.text"

# Create a new File object and load the CSV file into a DataSet.
MyFile = FileClass(file_name)
reader = MyFile.read_csv()

# Create a new Calculator object.
MyCalculator = CalculatorClass()

# Calculate totals scores
title = "Financial analysis"
totalMonths = MyCalculator.getTotalMonths(reader)    
netAmount = MyCalculator.getNetAmountByColumn(reader, "Profit/Losses")
averageChange = MyCalculator.getAverageChange(reader, "Profit/Losses")
greatestProfitLabel, greatestProfit = MyCalculator.getGreatestProfit(reader, "Date", "Profit/Losses")
lowestLabel, lowestProfit = MyCalculator.getLowestProfit(reader, "Date", "Profit/Losses")

# Print Screen Results
print(title.upper())
print('-' * (len(title) + 5))

print(f"Total Months: {totalMonths}")

print(f"Total: ${netAmount}")

print(f"Average  Change: ${averageChange}")

print(f"Greatest Increase in Profits: {greatestProfitLabel} (${greatestProfit})")

print(f"Greatest Decrease in Profits: {lowestLabel} (${lowestProfit})")

# Export Results 
MyFile.exportToTextFile(fileExport, title, totalMonths, netAmount, averageChange, greatestProfitLabel, greatestProfit, lowestLabel, lowestProfit)
