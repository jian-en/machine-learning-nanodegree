# As with the previous exercises, let's look at the performance of a couple of classifiers
# on the familiar Titanic dataset. Add a train/test split, then store the results in the
# dictionary provided.

import numpy as np
import pandas as pd

# Load the dataset
X = pd.read_csv('titanic_data.csv')

X = X._get_numeric_data()
y = X['Survived']
del X['Age'], X['Survived']


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score as recall
from sklearn.metrics import precision_score as precision
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation


# TODO: split the data into training and testing sets,
# using the standard settings for train_test_split.
# Then, train and test the classifiers with your newly split data instead of X and y.
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.4, random_state=0)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
print "Decision Tree recall: {:.2f} and precision: {:.2f}".format(recall(clf.predict(X_test),y_test),precision(clf.predict(X_test),y_test))

clf = GaussianNB()
clf.fit(X_train, y_train)
print "GaussianNB recall: {:.2f} and precision: {:.2f}".format(recall(clf.predict(X_test),y_test),precision(clf.predict(X_test),y_test))

results = {
  "Naive Bayes Recall": 0,
  "Naive Bayes Precision": 0,
  "Decision Tree Recall": 0,
  "Decision Tree Precision": 0
}
