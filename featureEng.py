import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

dataframe = pd.read_csv('F:/Python/TS/DataCode/daily-total-female-births-CA.csv',parse_dates=[0])
# print(dataframe.head())

feature = dataframe.copy();
# plt.plot(dataframe)
# plt.show()
zoomedDataframe = dataframe[(dataframe['date']>'1959-01-01') & (dataframe['date']<='1959-01-10')].copy()
plt.plot(zoomedDataframe.date,zoomedDataframe.births)
plt.show()
feature['year'] = dataframe['date'].dt.year
feature['month'] = dataframe['date'].dt.month
feature['day'] = dataframe['date'].dt.day

feature['lags'] = dataframe['births'].shift(1)

feature['MA 2'] = dataframe['births'].rolling(window=2).mean()

feature['max']=dataframe['births'].expanding().max()

print(feature.head(10))


