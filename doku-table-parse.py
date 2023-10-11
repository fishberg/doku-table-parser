#!/usr/bin/env python

import pandas as pd
import io
import argparse

def doku2csv(s):
    s = s.replace('^','|')
    rows = []
    for line in s.split('\n'):
        split = line.strip().split('|')[1:-1]
        row = []
        for col in split:
            row.append(col.strip())
        rows.append(','.join(row))
    return '\n'.join(rows)

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', default='input.txt', type=str, help='path to doku table text file; defaults to "input.txt"')
parser.add_argument('--cols', '-c', type=str, action='append', help='column(s) to print, repeatable; if completely omitted, prints column names')
args = parser.parse_args()

# --------------------------------------

with open(args.input) as READ:
    DATA = READ.read()

csv = doku2csv(DATA)
df = pd.read_csv(io.StringIO(csv))

# --------------------------------------

if args.cols is None:
    for i in df.columns:
        print(i)
else:
    print(df[args.cols])
