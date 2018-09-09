import csv
import operator

fname = "./data/budget_data.csv"
fileExport = "./pyBank/budget_data.text"

def read_csv(files_reader):
    csv_data = []
    for row in files_reader:
        csv_data.append(row)
    return csv_data

def getTotalMonths(data):
    totalValues = len(list(data))
    return totalValues

def getNetAmountByColumn(data, columnName):
    netAmount = 0
    list1 = [element.get(columnName) for element in data]
    iterateUntil = len(list1)

    for item in range(0, iterateUntil):
        netAmount += int(list1[item])

    return netAmount


def getAverageChange(data, columnName):
    resultList = []
    columnList = [element.get(columnName) for element in data]
    iterateUntil = len(columnList)

    for item in range(1, iterateUntil):
        normalValue = float(columnList[item]) - float(columnList[item - 1])
        resultList.append(normalValue)

    return round(sum(resultList) / len(resultList), 2)

def getGreatestProfit(data, columnKey, columnValue):
    resultList = {}
    iterateUntil = len(data)

    for item in range(1, iterateUntil):
        currentValue = data[item].get(columnValue)
        previousValue = data[item - 1].get(columnValue)

        normalValue = int(currentValue) - int(previousValue)
        resultList[data[item].get("Date")] = normalValue

    maxKey = max(resultList.items(), key = operator.itemgetter(1))[0]
    maxValue = max(resultList.items(), key = operator.itemgetter(1))[1]
    
    return maxKey, maxValue

def getLowestProfit(data, columnKey, columnValue):
    resultList = {}
    iterateUntil = len(data)

    for item in range(1, iterateUntil):
        currentValue = data[item].get(columnValue)
        previousValue = data[item - 1].get(columnValue)

        normalValue = int(currentValue) - int(previousValue)
        resultList[data[item].get("Date")] = normalValue

    maxKey = min(resultList.items(), key = operator.itemgetter(1))[0]
    maxValue = min(resultList.items(), key = operator.itemgetter(1))[1]
    
    return maxKey, maxValue

def writeResultsTextFile(file_name, title, totalMonths, netAmount, averageChange, greatestProfitLabel, greatestProfit, lowestLabel, lowestProfit):
    with open(file_name, "w") as file:    
        file.write(title.upper())
        file.write('\n')

        file.write('-' * (len(title) + 5))
        file.write('\n')

        file.write(f"Total Months: {totalMonths}")
        file.write('\n')

        file.write(f"Total: ${netAmount}")
        file.write('\n')

        file.write(f"Average  Change: ${averageChange}")
        file.write('\n')

        file.write(f"Greatest Increase in Profits: {greatestProfitLabel} (${greatestProfit})")
        file.write('\n')

        file.write(f"Greatest Decrease in Profits: {lowestLabel} (${lowestProfit})")     
        file.write('\n')



with open(fname) as f:
    # Gets the CSV file values.
    reader = read_csv(csv.DictReader(f))

# Calculate totals scores
title = "Financial analysis"
totalMonths = getTotalMonths(reader)    
netAmount = getNetAmountByColumn(reader, "Profit/Losses")
averageChange = getAverageChange(reader, "Profit/Losses")
greatestProfitLabel, greatestProfit = getGreatestProfit(reader, "Date", "Profit/Losses")
lowestLabel, lowestProfit = getLowestProfit(reader, "Date", "Profit/Losses")

# Print Screen Results
print(title.upper())
print('-' * (len(title) + 5))

print(f"Total Months: {totalMonths}")

print(f"Total: ${netAmount}")

print(f"Average  Change: ${averageChange}")

print(f"Greatest Increase in Profits: {greatestProfitLabel} (${greatestProfit})")

print(f"Greatest Decrease in Profits: {lowestLabel} (${lowestProfit})")

# Export Results 
writeResultsTextFile(fileExport, title, totalMonths, netAmount, averageChange, greatestProfitLabel, greatestProfit, lowestLabel, lowestProfit)
