import numpy as np
import pandas as pd

# Load the dataset
from sklearn.datasets import load_linnerud

linnerud_data = load_linnerud()
X = linnerud_data.data
y = linnerud_data.target

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn import cross_validation

# TODO: split the data into training and testing sets,
# using the standard settings for train_test_split.
# Then, train and test the classifiers with your newly split data instead of X and y.
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.4, random_state=0)

reg = DecisionTreeRegressor()
reg.fit(X_train, y_train)
print "Decision Tree mean absolute error: {:.2f}".format(mse(reg.predict(X_test),y_test))

reg = LinearRegression()
reg.fit(X_train, y_train)
print "Linear regression mean absolute error: {:.2f}".format(mse(reg.predict(X_test),y_test))

results = {
 "Linear Regression": 0,
 "Decision Tree": 0
}
