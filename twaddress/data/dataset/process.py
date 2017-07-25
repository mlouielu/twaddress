# -*- coding: utf-8 -*-

import csv


def to_dict(path, output, key):
    # To jieba dict
    with open(path, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        with open(output, 'a') as outfile:
            for row in reader:
                outfile.write('%s 100 v\n' % (row[key]))


if __name__ == '__main__':
    to_dict('county10603.csv', 'out.csv', 1)
    to_dict('road10603.csv', 'out.csv', 0)
    to_dict('village10602.csv', 'out.csv', 0)
