from sklearn.naive_bayes import GaussianNB


def classify(features_train, labels_train):
    gnb = GaussianNB()
    return gnb.fit(features_train, labels_train)
