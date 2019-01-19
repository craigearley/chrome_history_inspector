#!/bin/python import pandas
import csv
import pandas as pd

delim = '/'
ROWS_TO_DISPLAY = 50

filename = 'my-history.csv'
f = open(filename)

history_df = pd.read_csv(filename)
history_df.columns = ['timestamp','url']
history_df['domain'] = history_df.url.str.replace('http://','').str.replace('https://','').str.replace('www.','')
history_df['domain'] = history_df.domain.str.split(delim).str.get(0)

counts = history_df.groupby('domain').count()
counts.columns = ['domain','count']

print(counts.sort_values(['count'], ascending=False).head(ROWS_TO_DISPLAY))