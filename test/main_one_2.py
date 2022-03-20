import csv

kospi = open('data/KOSPI Historical Data.csv','r')
kospi_csv = csv.reader(kospi)

for line in kospi_csv:
    print(line)
kospi.close()    