# In this exercise, we'll use the Titanic dataset as before, train two classifiers and
# look at their confusion matrices. Your job is to create a train/test split in the data
# and report the results in the dictionary at the bottom.

import pandas as pd

X = pd.read_csv('titanic_data.csv')

X = X._get_numeric_data()
y = X['Survived']
del X['Age'], X['Survived']


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation

# TODO: split the data into training and testing sets,
# using the standard settings for train_test_split.
# Then, train and test the classifiers with your newly split data instead of X and y.
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y)

clf = DecisionTreeClassifier()
clf.fit(X_train,y_train)
print "Confusion matrix for this Decision Tree:\n",confusion_matrix(clf.predict(X_test),y_test)

clf = GaussianNB()
clf.fit(X_train,y_train)
print "GaussianNB confusion matrix:\n",confusion_matrix(clf.predict(X_test),y_test)
