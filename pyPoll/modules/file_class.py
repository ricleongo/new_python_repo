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

    def exportToTextFile(self, file_name, title, totalVotes, candidatesScored, winner, separator):

        with open(file_name, "w") as file:  
            file.write(title)
            file.write('\n')

            file.write(separator)
            file.write('\n')
        
            file.write(f"Total Votes: {totalVotes}")
            file.write('\n')

            file.write(separator)
            file.write('\n')

            for k,v in candidatesScored:
                percentage = round((v / totalVotes) * 100, 3)
                file.write(f"{k}: {percentage}% ({v})")
                file.write('\n')

            file.write(separator)
            file.write('\n')

            file.write(f"Winner: {winner}")
            file.write('\n')

            file.write(separator)   
            file.write('\n')
