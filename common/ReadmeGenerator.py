#!/usr/bin/env python
# coding: utf-8

import csvtomd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


###     Generating performance charts
#################################################

#Function to plot a performance chart
def plot_perf(x,y,df):

    # extract submission name from submission URL
    labels = df.apply(lambda x: x['Submission Name'][1:].split(']')[0], axis=1)

    fig = plt.scatter(x=df[x],y=df[y], label=labels, s=150, alpha = 0.5,
             c= ['b', 'g', 'r', 'c', 'm', 'y', 'k'])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(y + ' by ' + x)
    offset = (max(df[y]) - min(df[y]))/50
    for i,name in enumerate(labels):
        ax = df[x][i]
        ay = df[y][i] + offset * (-2.5 + i % 5)
        plt.text(ax, ay, name, fontsize=10)
    
    return(fig)

###       Printing the Readme.md file
############################################
readmefile = '../Readme.md'
#Wrtie header 
#print(file=open(readmefile))
print('# TSPerf\n', file=open(readmefile, "w"))

print('TSPerf is a framework that allows discovery and comparison of various time-series forecasting algorithms and architectures on a cloud-based environment. This framework allows data scientists to discover the best approach that fits their use case from cost, time and quality perspective.\n TSPerf framework is designed to facilitate data science community participation and contribution through the development of benchmark implementations against a given set of forecasting problems and datasets. Benchmark implementations are measured in terms of standard metrics of model accuracy, training cost and model training time. Each implementation includes all the necessary instructions and tools that ensure its reproducibility on Azure customer\'s subscription. We plan to leverage TSPerf to propose a new time-series forecasting track in [MLPerf](https://mlperf.org/).', file=open(readmefile, "a"))

print('The following table summarizes benchmarks that are currently included in TSPerf.\n',  file=open(readmefile, "a")) 

#Read the benchmark table the CSV file and converrt to a table in md format
with open('Benchmarks.csv', 'r') as f:
                table = csvtomd.csv_to_table(f, ',')
print(csvtomd.md_table(table), file=open(readmefile, "a"))
print('\n\n\n',file=open(readmefile, "a"))

print('A complete documentation of TSPerf, along with the instructions for submitting and reviewing benchmark implementations, can be found [here](./docs/tsperf_rules.md). The tables below show performance of benchmark implementations that are developed so far. These tables are referred to as *performance boards*. Source code of benchmark implementations and instructions for reproducing their performance can be found in submission folders, which are linked in the last column of performance boards.\n', file=open(readmefile, "a"))

### Write the Energy section
#============================

print('## Probabilistic energy forecasting performance board\n\n', file=open(readmefile, "a"))
print('The following table lists the current submision for the energy foercasting and their respective performances.\n\n', file=open(readmefile, "a")) 

#Read the energy perfromane board from the CSV file and converrt to a table in md format
with open('TSPerfBoard-Energy.csv', 'r') as f:
                table = csvtomd.csv_to_table(f, ',')
print(csvtomd.md_table(table), file=open(readmefile, "a"))

#Read Energy Performance  Board CSV file
df = pd.read_csv('TSPerfBoard-Energy.csv',  engine='python')
#df

#Plot ,'Pinball Loss' by 'Training and Scoring Cost($)' chart
fig4 = plt.figure(figsize=(12, 8), dpi= 80, facecolor='w', edgecolor='k') #this sets the plotting area size
fig4 = plot_perf('Training and Scoring Cost($)','Pinball Loss',df)
plt.savefig('../docs/images/Energy-Cost.png')


#insetting the performance charts
print('\n\nThe following chart compares the submissions performance on accuracy in Pinball Loss vs. Training and Scoring cost in $:\n\n ', file=open(readmefile, "a"))
print('![EnergyPBLvsTime](./docs/images/Energy-Cost.png)' ,file=open(readmefile, "a"))
print('\n\n\n',file=open(readmefile, "a"))


#print the retail sales forcsating section
#========================================
print('## Retail sales forecasting performance board\n\n', file=open(readmefile, "a"))
print('The following table lists the current submision for the retail foercasting and their respective performances.\n\n', file=open(readmefile, "a")) 

#Read the energy perfromane board from the CSV file and converrt to a table in md format
with open('TSPerfBoard-Retail.csv', 'r') as f:
                table = csvtomd.csv_to_table(f, ',')
print(csvtomd.md_table(table), file=open(readmefile, "a"))
print('\n\n\n',file=open(readmefile, "a"))

#Read  Retail Performane Board CSV file
df = pd.read_csv('TSPerfBoard-Retail.csv',  engine='python')
#df

#Plot MAPE (%) by Training and Scoring Cost ($) chart
fig2 = plt.figure(figsize=(12, 8), dpi= 80, facecolor='w', edgecolor='k') #this sets the plotting area size
fig2 = plot_perf('Training and Scoring Cost ($)','MAPE (%)',df)
plt.savefig('../docs/images/Retail-Cost.png')


#insetting the performance charts
print('\n\nThe following chart compares the submissions performance on accuracy in %MAPE vs. Training and Scoring cost in $:\n\n ', file=open(readmefile, "a"))
print('![EnergyPBLvsTime](./docs/images/Retail-Cost.png)' ,file=open(readmefile, "a"))
print('\n\n\n',file=open(readmefile, "a"))



print('A new Readme.md file has been generated successfuly.')     


