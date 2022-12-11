import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

tempDatabase = pd.read_csv('F:/Python/TS/DataCode/daily-min-temperatures.csv',
                            parse_dates=[0])

train,test = tempDatabase[:len(tempDatabase)-7],tempDatabase[len(tempDatabase)-7:]

from statsmodels.tsa.stattools import adfuller
stationarity_test = adfuller(tempDatabase.Temp, autolag='AIC')

from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
# plot_pacf(tempDatabase.Temp, lags=40)
# plt.show()

from statsmodels.tsa.ar_model import AutoReg
model = AutoReg(train.Temp, lags=29)
fittedModel = model.fit()

print(fittedModel.summary())

testForecast = fittedModel.predict(start= len(train), end= len(tempDatabase)-1, dynamic=False)
print(testForecast)
print(test)

from sklearn.metrics import mean_squared_error
from math import sqrt
mse = mean_squared_error(testForecast,test['Temp'])
print(sqrt(mse))

plt.plot(test['Temp'],'b',label= 'Test Data Set')
plt.plot(testForecast,'r',  label= 'Test Forecast')
plt.legend()
plt.show()
# Future Forecast

forecast= fittedModel.predict(start=len(tempDatabase)-1 , end= len(tempDatabase)+7)
print(forecast)


