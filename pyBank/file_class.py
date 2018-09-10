import csv

class FileClass():

    def __init__(self, file_name):
        self.file_name = file_name

    def read_csv(self):
        csv_data = []

        with open(self.file_name) as f:
            # Gets the CSV file values.
            file_reader = csv.DictReader(f)

            for row in file_reader:
                csv_data.append(row)

        return csv_data

    def exportToTextFile(self, file_name, title, totalMonths, netAmount, averageChange, greatestProfitLabel, greatestProfit, lowestLabel, lowestProfit):

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
