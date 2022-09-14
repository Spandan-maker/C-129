import csv

data1 = []
data2 = []

with open("final.csv", 'r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        data1.append(row)

header1 = data1[0]
planetData1 = data1[1:]

with open("new_dataset2.csv", 'r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        data2.append(row)

header2 = data2[0]
planetData2 = data2[1:]

headers = header1 + header2

planetData = []

for index, row in enumerate(planetData1):
    planetData.append(planetData1[index] + planetData2[index])


with open("merged_dataset.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planetData)