import re
import csv

file = open("dataset.csv", "r")
reader = csv.reader(file, delimiter='+')
tokenize = {}
no_of_items = {}
feature_set = {}

for row in reader:
    no_of_items.setdefault(row[1], 0)
    no_of_items[row[1]] += 1
    # Tokenize the data
    tokenize.setdefault(row[1], {})
    split_data = re.split('[^a-zA-Z\']', row[0])
    for i in split_data:
        if len(i) > 2:
            tokenize[row[1]].setdefault(i.lower(), 0)
            tokenize[row[1]][i.lower()] += 1
            feature_set.setdefault(i.lower(), {})
            feature_set[i.lower()].setdefault(row[1], 0)
            feature_set[i.lower()][row[1]] += 1
    # print((tokenize))