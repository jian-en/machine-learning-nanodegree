import numpy as np
import pandas as pd

import visuals as vs
from sklearn.cross_validation import ShuffleSplit

data = pd.read_csv('housing.csv')

prices = data['MEDV']
features = data.drop('MEDV', axis=1)

print "Boston housing dataset has {} data points with {} variables each.".format(*data.shape)

minimum_price = np.min(prices)

maximum_price = np.max(prices)

mean_price = np.mean(prices)

median_price = np.median(prices)

std_price = np.std(prices)

# Show the calculated statistics
print "Statistics for Boston housing dataset:\n"
print "Minimum price: ${:,.2f}".format(minimum_price)
print "Maximum price: ${:,.2f}".format(maximum_price)
print "Mean price: ${:,.2f}".format(mean_price)
print "Median price ${:,.2f}".format(median_price)
print "Standard deviation of prices: ${:,.2f}".format(std_price)
