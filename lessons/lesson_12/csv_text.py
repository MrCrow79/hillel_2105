import csv


import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]


with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)  # instead of csvfile.write()
    writer.writerows(data)

with open('data.csv', newline='') as f:
    x = f.read()
    # print(x)

with open('data.csv', newline='') as f:

    reader = csv.reader(f)  #  instead of f.read()
    for row in reader:
        print(', '.join(row))