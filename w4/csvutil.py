import csv

""" To read csv from disk using csv library and return each row as a string.
Assumption: "," delimiter.

"""
def fetchLines(fileName):
    with open(fileName) as csv_file:
        csvRows = ''
        readerElements = csv.reader(csv_file, delimiter=',')
        for row in readerElements:
            csvRows = csvRows + str(row) + "\n"

    return csvRows

print( fetchLines("data\weather.csv"))