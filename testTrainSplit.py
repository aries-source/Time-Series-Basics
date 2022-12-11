import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

tempDatabase = pd.read_csv('F:/Python/TS/DataCode/daily-min-temperatures.csv',
                            parse_dates=[0])

print(tempDatabase.head())
print(tempDatabase.tail())

trainSize = int(tempDatabase.shape[0]*0.8)
print(trainSize)

trainDataset = tempDatabase[0:trainSize]

print(trainDataset.tail())

testDataset = tempDatabase[trainSize:]
print(testDataset.head())

print(trainDataset.shape)
print(testDataset.shape)


