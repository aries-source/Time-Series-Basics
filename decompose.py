import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

birthsDataframe = pd.read_csv('F:/Python/TS/DataCode/daily-total-female-births-CA.csv',
                    parse_dates=[0])

milesDataframe = pd.read_csv('F:/Python/TS/DataCode/us-airlines-monthly-aircraft-miles-flown.csv',
                        parse_dates=[0])

from statsmodels.tsa.seasonal import seasonal_decompose
birthsDataframe.index = birthsDataframe.date
milesDataframe.index = milesDataframe.Month
decompose = seasonal_decompose(milesDataframe['MilesMM'], model='additive')

decompose_2 =seasonal_decompose(birthsDataframe['births'], model='additive')

decompose.plot()
plt.show()

decompose_2.plot()
plt.show()

#We could plot the individual components separately using the following code
decompose.seasonal.plot()
decompose.trend.plot()
decompose.resid.plot()


