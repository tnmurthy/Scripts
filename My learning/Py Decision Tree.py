# Run this program on your local python
# interpreter, provided you have installed the required libraries.

## Terms used in code :

# Gini index and information gain both of these methods are used to select
# from the n attributes of the dataset which attribute would be placed at the root node or the internal node.
# Gini Index is a metric to measure how often a randomly chosen element would be incorrectly identified.

# Entropy is the measure of uncertainty of a random variable,
# it characterizes the impurity of an arbitrary collection of examples.
# The higher the entropy the more the information content.

# Information Gain entropy typically changes when we use a node in a decision tree to partition the training instances into smaller subsets.
# Information gain is a measure of this change in entropy. Sklearn supports “entropy” criteria for Information Gain and
# if we want to use Information Gain method in sklearn then we have to mention it explicitly.
# Accuracy score is used to calculate the accuracy of the trained classifier.
# Confusion Matrix is used to understand the trained classifier behavior over the test dataset or validate dataset.

# Importing the required packages
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Function importing Dataset
def importdata():
    balance_data = pd.read_csv (
        'https://archive.ics.uci.edu/ml/machine-learning-' +
        'databases/balance-scale/balance-scale.data',
        sep=',', header=None)

    # Printing the dataswet shape
    print ("Dataset Lenght: ", len (balance_data))
    print ("Dataset Shape: ", balance_data.shape)

    # Printing the dataset obseravtions
    print ("Dataset: ", balance_data.head ())
    return balance_data

# Function to split the dataset
def splitdataset(balance_data):
    # Seperating the target variable
    X = balance_data.values[:, 1:5]
    Y = balance_data.values[:, 0]

    # Spliting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split (
        X, Y, test_size=0.3, random_state=100)

    return X, Y, X_train, X_test, y_train, y_test

# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier (criterion="gini",
                                       random_state=100, max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_gini.fit (X_train, y_train)
    return clf_gini

# Function to perform training with entropy.
def tarin_using_entropy(X_train, X_test, y_train):
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier (
        criterion="entropy", random_state=100,
        max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_entropy.fit (X_train, y_train)
    return clf_entropy

# Function to make predictions
def prediction(X_test, clf_object):
    # Predicton on test with giniIndex
    y_pred = clf_object.predict (X_test)
    print ("Predicted values:")
    print (y_pred)
    return y_pred

# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
    print ("Confusion Matrix: ",
           confusion_matrix (y_test, y_pred))

    print ("Accuracy : ",
           accuracy_score (y_test, y_pred) * 100)

    print ("Report : ",
           classification_report (y_test, y_pred))

# Driver code
def main():
    # Building Phase
    data = importdata ()
    X, Y, X_train, X_test, y_train, y_test = splitdataset (data)
    clf_gini = train_using_gini (X_train, X_test, y_train)
    clf_entropy = tarin_using_entropy (X_train, X_test, y_train)

    # Operational Phase
    print ("Results Using Gini Index:")

    # Prediction using gini
    y_pred_gini = prediction (X_test, clf_gini)
    cal_accuracy (y_test, y_pred_gini)

    print ("Results Using Entropy:")
    # Prediction using entropy
    y_pred_entropy = prediction (X_test, clf_entropy)
    cal_accuracy (y_test, y_pred_entropy)

# Calling main function
if __name__ == "__main__":
    main ()
