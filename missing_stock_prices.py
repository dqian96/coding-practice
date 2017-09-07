# Problem: Missing Stock Prices

"""

You are given time series data for a stock. Each point is the highest price for said stock that day.
Some days (20) have missing data - the highest stock price is missing for said day. Estimate the
highest stock price for those days.

More specifically, you are first given "n", the number of lines to follow.

Each non-price-missing line is an entry like so:

"1/3/2012 16:00:00	26.96"
i.e. the date and time followed by the highest stock price for said day


Each price-missing line is an entry like so:
"5/24/2012 16:00:00	Missing_4"
i.e. the date and time followed by Missing_i

Output the predicted highest stock price for each of the missing days, in order like so:

27.123
323.11
...
23.123

A score will be given based on the deviation of your results and the actual stock prices.

Solution:

Transform the given data into features X and expected output y.

For each line, the feature is simply the number of days between the date of the given line and the
earliest date given.

The expected output is the highest stock price of the line.

We use a polynomial regression in order to predict the missing values.
This was able to pass 2/3 test cases.

Suggestion for improvement: Since there are no prices for Saturday and Sunday, 
then if Friday was day n, Monday should be day n + 1. Currently, Monday is n + 3.

"""

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sys import stdin
import datetime

def parse(log_line):
    tokens = log_line.split()
    
    date_info = tokens[0].split("/")
    date = datetime.date(int(date_info[-1]), int(date_info[-3]), int(date_info[-2]))
    
    price = (None if tokens[2][0] == 'M' else float(tokens[2]))
    
    return (date, price)
    

def create_data_set():
    earliest_date = None
    n = int(stdin.readline())
    X = []
    y = []
    missing_x = []
    for i in range(n):
        log_data = parse(stdin.readline())
        if earliest_date is None:
            earliest_date = log_data[0]
        if log_data[1] is None:
            # missing price
            missing_x.append((log_data[0] - earliest_date).days)
            continue
        X.append((log_data[0] - earliest_date).days)
        y.append(log_data[1])
    
    return ((X, y), missing_x)

def build_model(data_set):
    model = np.poly1d(np.polyfit(data_set[0], data_set[1], 120))

    # neural_network = MLPRegressor()
    # neural_network.fit(data_set[0], data_set[1])
    return model

def predict_prices(model, days):
    prices = []
    for day in days:
        # prices.append(model.predict(np.array([day]).reshape(-1, 1))[0])
        prices.append(model(day))
    return prices

def main():
    data_set = create_data_set()
    model = build_model(data_set[0])
    predictions = predict_prices(model, data_set[1])

    for p in predictions:
        print(p)

main()
