from turtle import right
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

birthsDataframe = pd.read_csv('F:/Python/TS/DataCode/daily-total-female-births-CA.csv',
                    parse_dates=[0])

milesDataframe = pd.read_csv('F:/Python/TS/DataCode/us-airlines-monthly-aircraft-miles-flown.csv',
                        parse_dates=[0])

plt.plot(birthsDataframe.date, birthsDataframe.births)
plt.show()

plt.plot(milesDataframe.Month,milesDataframe.MilesMM)
plt.show()

sns.regplot(x=milesDataframe.index.values, y=milesDataframe.MilesMM)
plt.show()

# sns.regplot(x=milesDataframe.index.values ,y=milesDataframe['MilesMM'])

from pandas.plotting import lag_plot
lag_plot(birthsDataframe.births)
plt.show()
lag_plot(milesDataframe.MilesMM)
plt.show()

from pandas.plotting import autocorrelation_plot
autocorrelation_plot(birthsDataframe.births)
plt.show()

autocorrelation_plot(milesDataframe.MilesMM)
plt.show()
