#!/bin/python import pandas
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data

delim = '/'
ROWS_TO_DISPLAY = 20

filename = 'my-history.csv'
f = open(filename)

history_df = pd.read_csv(filename)
history_df.columns = ['timestamp','url']
history_df['domain'] = history_df.url.str.replace('http://','').str.replace('https://','').str.replace('www.','')
history_df['domain'] = history_df.domain.str.split(delim).str.get(0).str.rsplit('.', 1).str.get(0)

counts = history_df.groupby(['domain']).size().reset_index(name='count')
#print(counts.sort_values('count', ascending=False).head(ROWS_TO_DISPLAY))

# plots

sns.set(style="whitegrid")
counts.sort_values('count',ascending=False).head(ROWS_TO_DISPLAY).plot(kind='bar',x='domain',y='count', legend=None)

figure = plt.gcf()
figure.set_size_inches(8,6)

plt.xlabel('site')
plt.ylabel('visit count')

plt.title('Your ' + str(ROWS_TO_DISPLAY) + ' Most Visited Sites')

plt.xticks(rotation=60)

plt.tight_layout()

plt.savefig('most_visited_sites.png')
