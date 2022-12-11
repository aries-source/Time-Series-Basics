import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

tempDatabase = pd.read_csv('F:/Python/TS/DataCode/daily-min-temperatures.csv',
                            parse_dates=[0])

train,test = tempDatabase[:len(tempDatabase)-7],tempDatabase[len(tempDatabase)-7:] 