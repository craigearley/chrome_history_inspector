#!/bin/python import pandas
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

delim = '/'
ROWS_TO_DISPLAY = 20

filename = 'my-history.csv'
f = open(filename)

history_df = pd.read_csv(filename)
history_df.columns = ['timestamp','url']
history_df['domain'] = history_df.url.str.replace('http://','').str.replace('https://','').str.replace('www.','')
history_df['domain'] = history_df.domain.str.split(delim).str.get(0)

counts = history_df.groupby(['domain']).size().reset_index(name='count')
print(counts.sort_values('count', ascending=False).head(ROWS_TO_DISPLAY))

sns.set(style="whitegrid")

counts.sort_values('count',ascending=False).head(ROWS_TO_DISPLAY).plot(kind='bar',x='domain',y='count')

plt.show()
