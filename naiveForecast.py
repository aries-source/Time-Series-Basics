from cProfile import label
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

tempDatabase = pd.read_csv('F:/Python/TS/DataCode/daily-min-temperatures.csv',
                            parse_dates=[0])

tempDatabase['Lag 1'] = tempDatabase['Temp'].shift(1)

train,test = tempDatabase[1:tempDatabase.shape[0]-7],tempDatabase[tempDatabase.shape[0]-7:]

testObserved= test['Temp']
testForecast= test['Lag 1']

from sklearn.metrics import mean_squared_error
Error = mean_squared_error(testObserved,testForecast)
print(Error)

plt.plot(testForecast,'b',label='Forecast')
plt.plot(testObserved,'r',label='Observed')
plt.legend()
plt.show()

