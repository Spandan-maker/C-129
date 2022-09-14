import csv
from dataclasses import field

data = []

with open("archive_dataset.csv", 'r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        data.append(row)

header = data[0]
planetData = data[1:]


for row in planetData:
    row[2] = row[2].lower()

planetData.sort(key = lambda planetData: planetData[2])

with open("new_dataset.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(planetData)
    
with open("new_dataset2.csv", 'w', newline = '') as f, open("new_dataset.csv", 'r') as e:
    writer = csv.writer(f)
    
    for row in csv.reader(e):
        if any(field.strip() for field in row):
            writer.writerow(row)
