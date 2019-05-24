import csv
import random


def parse_csv(filename):
    resulting_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] == '0' or row[1] == '1' or row[1] == '2':
                resulting_list.append((row[0], row[1]))
    return resulting_list
