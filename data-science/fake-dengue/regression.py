#!/usr/bin/env python3

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

DATA_FILE_NAME = 'data.csv'

file = pd.read_csv(DATA_FILE_NAME)

years = file[['year']]
cases = file[['cases']]

linearRegression = LinearRegression()
linearRegression.fit(X=years, y=cases)

future_year = [[2018]]
cases_in_2018 = linearRegression.predict(future_year)

print('cases expected for 2018:', int(cases_in_2018))

plt.scatter(years, cases, color='black')
plt.scatter(future_year, cases_in_2018, color='red')
plt.plot(years, linearRegression.predict(years), color='blue')

plt.xlabel('Years')
plt.ylabel('Cases')
plt.xticks([2018])
plt.yticks([int(cases_in_2018)])

plt.show()
