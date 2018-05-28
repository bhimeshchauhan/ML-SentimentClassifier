import re
import csv

file = open("training_data.csv", "r")
reader = csv.reader(file, delimiter='+')
tokenize = {}
labels = {}
feature = {}

for row in reader:
    print("looping ", len(row), "  ", row)
    if len(row)==1:
        row.append('-1,,,,,,,')
    labels.setdefault(row[1], 0)
    print("debug")
    labels[row[1]] += 1
    # Tokenize the data
    tokenize.setdefault(row[1], {})
    split_data = re.split('[^a-zA-Z\']', row[0])
    for i in split_data:
        if len(i) > 2:
            tokenize[row[1]].setdefault(i.lower(), 0)
            tokenize[row[1]][i.lower()] += 1
            feature.setdefault(i.lower(), {})
            feature[i.lower()].setdefault(row[1], 0)
            feature[i.lower()][row[1]] += 1
        # print((tokenize))
        # print(len(labels))
        # print("ROWWWWW ", row[1])