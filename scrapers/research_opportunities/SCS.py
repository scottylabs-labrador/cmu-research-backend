import csv

# Goal: parse json
with open('scrapers/research_opportunities/example_json/Simple Undergrad.csv', mode ='r') as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines["Date Added"])
