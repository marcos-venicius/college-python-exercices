#!/usr/bin/env python3

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

def get_year(years) -> int:
    min_year = int(years.iloc[0]['year']) + 1

    year = input('prediction year: ')

    if year is None or not year.isnumeric() or int(year) < min_year:
        print(f'[!] invalid year. must be greater than or equal to {min_year}')
        return get_year(years)

    return int(year)


DATA_FILE_NAME = 'data.csv'

file = pd.read_csv(DATA_FILE_NAME)

years = file[['year']]
cases = file[['cases']]

linearRegression = LinearRegression()
linearRegression.fit(X=years, y=cases)

prediction_year = get_year(years)

future_year = [[prediction_year]]
cases_in_prediction_year = linearRegression.predict(future_year)

print(f'cases expected for {prediction_year}:', int(cases_in_prediction_year))

plt.scatter(years, cases, color='black')
plt.scatter(future_year, cases_in_prediction_year, color='red')
plt.plot(years, linearRegression.predict(years), color='blue')

plt.xlabel('Years')
plt.ylabel('Cases')
plt.xticks([prediction_year])
plt.yticks([int(cases_in_prediction_year)])

plt.show()
