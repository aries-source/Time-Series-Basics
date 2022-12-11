import numpy as np;
import matplotlib.pyplot as plt;
import pandas as pd;
import seaborn as sns;

name = 'Julian'
print('My name is {}'.format(name))

type(name)
new_name=name.replace('Julian','Harrison')
print(new_name)

lis = [0,1,2,3,4,5,6,7,8,9]
print(lis[0::2])
for i in range(0,10,1):
    print(i)

lis.insert(-1,8.5)
print(lis)


dict ={
    'name': 'Julian',
    'age': 24,
    'school': 'knust',
    'program':'Statistics'
}

data = pd.read_csv('F:/Python/TS/DataCode/daily-total-female-births-CA.csv',index_col=0,parse_dates=[0],squeeze=True)
print(data.head(10))
print(data.loc['1959-01'])

print(data.describe())
print(data.iloc[2])

house_price = pd.read_csv('House_Price.csv', header = 0)
print(house_price.head(10))

sns.displot(data , kde=False)
sns.pairplot(house_price)
plt.show()

# customers = pd.read_csv('F:/Python/TS/Python CC/customer.csv')
# print(customers.head(10))
# print(customers.Age)

# cust = pd.read_csv('F:/Python/TS/Python CC/customer.csv', index_col= 0)

