import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

birthsDataframe = pd.read_csv('F:/Python/TS/DataCode/daily-total-female-births-CA.csv',
                    parse_dates=[0])

milesDataframe = pd.read_csv('F:/Python/TS/DataCode/us-airlines-monthly-aircraft-miles-flown.csv',
                        parse_dates=[0])


birthsDataframe['Lag 1'] = birthsDataframe.births.diff(periods=1)
# print(birthsDataframe.head(10))


from statsmodels.tsa.seasonal import seasonal_decompose
birthsDataframe.index = birthsDataframe.date
print(birthsDataframe.head(10))
# print(birthsDataframe.columns.tolist())
decompose  = seasonal_decompose(birthsDataframe.iloc[1: ,2])

milesDataframe['Lag 12'] = milesDataframe.MilesMM.diff(periods=12)
milesDataframe.index = milesDataframe.Month
print(milesDataframe.head(15))

decompose2 = seasonal_decompose(milesDataframe.iloc[12:,2])

decompose2.plot()
plt.show()


decompose.plot()
plt.show()