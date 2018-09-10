# Import Libraries to be used.
from modules.file_class import FileClass
from modules.calculator_class import CalculatorClass

# Define internal variables
file_name = "./pyPoll/data/election_data.csv"
fileExport = "./pyPoll/data/election_data.text"
column_name = 'Candidate'
separator = "-" * 25
report_title = "Election Results"

# Load CSV file and get dataset.
MyFile = FileClass(file_name)
DataSet = MyFile.read_csv()

# Create MyCalculator object.
MyCalculator = CalculatorClass()

# Get calculated values.
totalVotes = MyCalculator.getTotalVotes(DataSet)
candidatesVoted = MyCalculator.getCandidateVoted(DataSet, column_name)
candidatesScored = MyCalculator.getCandidateScoreByName(DataSet, column_name, candidatesVoted)
winner = MyCalculator.getCandidateWinner(candidatesScored)

# Print results in screen.
print(report_title)
print(separator)
print(f"Total Votes: {totalVotes}")
print(separator)

for k,v in candidatesScored:
    percentage = round((v / totalVotes) * 100, 3)
    print(f"{k}: {percentage}% ({v})")

print(separator)
print(f"Winner: {winner}")
print(separator)

# Export results
MyFile.exportToTextFile(fileExport, report_title, totalVotes, candidatesScored, winner, separator)
