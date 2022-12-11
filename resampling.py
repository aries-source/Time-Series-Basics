from turtle import right
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

dataframe = pd.read_csv('F:/Python/TS/DataCode/us-airlines-monthly-aircraft-miles-flown.csv',
                        parse_dates=[0])

# print(dataframe.head())

downSampling = dataframe.resample('Q',on='Month').mean()
print(downSampling.head(10))

downSamplingAnnually = dataframe.resample('A',on='Month').sum()
print(downSamplingAnnually.head(10))

upSampling = dataframe.resample('D',on='Month').mean()
print(upSampling.head(10))
print(upSampling.columns.tolist())

interpolatedUpSample = upSampling.interpolate(method='linear')
# print(interpolatedUpSample.head(10))

splineUpSample = upSampling.interpolate(method='spline', order=2)
# print(splineUpSample.head(10))
# print(splineUpSample.columns.tolist())
# zoomedSplineUpSample = splineUpSample[(splineUpSample['Month'] >='1963-01-01') 
#                             & (splineUpSample['Month'] <='1963-12-31')].copy()
# print(splineUpSample.head(10))
plt.plot(splineUpSample)
plt.show()

