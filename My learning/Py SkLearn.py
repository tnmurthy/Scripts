# Features: (also known as predictors, inputs, or attributes) they are simply the variables of our data.
# They can be more than one and hence represented by a feature matrix (‘X’ is a common notation to represent feature matrix).
# A list of all the feature names is termed as feature names.

# Response: (also known as the target, label, or output) This is the output variable depending on the feature variables.
# We generally have a single response column and it is represented by a response vector (‘y’ is a common notation to represent response vector).
# All the possible values taken by a response vector is termed as target names.

# load the iris dataset as an example
from sklearn.datasets import load_iris
iris = load_iris ()

# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target

# store the feature and target names
feature_names = iris.feature_names
target_names = iris.target_names

# printing features and target names of our dataset
print ("Feature names:", feature_names)
print ("Target names:", target_names)

# X and y are numpy arrays
print ("\nType of X is:", type (X))

# printing first 5 input rows
print ("\nFirst 5 rows of X:\n", X[:5])

# In pandas, important data types are:
# Series: Series is a one-dimensional labeled array capable of holding any data type.
# DataFrame: It is a 2-dimensional labeled data structure with columns of potentially different types.
# You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object.

import pandas as pd

# reading csv file
data = pd.read_csv ('C:/Users/saanvi/PycharmProjects/Scripts/My learning/weather.csv')

# shape of dataset
print ("Shape:", data.shape)

# column names
print ("\nFeatures:", data.columns)

# storing the feature matrix (X) and response vector (y)
X = data[data.columns[:-1]]
y = data[data.columns[-1]]

# printing first 5 rows of feature matrix
print ("\nFeature matrix:\n", X.head ())

# printing first 5 values of response vector
print ("\nResponse vector:\n", y.head ())

# Split the dataset into two pieces: a training set and a testing set.
# Train the model on the training set.
# Test the model on the testing set, and evaluate how well our model did.
# Advantages of train/test split:
#
# Model can be trained and tested on different data than the one used for training.
# Response values are known for the test dataset, hence predictions can be evaluated
# Testing accuracy is a better estimate than training accuracy of out-of-sample performance.

# load the iris dataset as an example
from sklearn.datasets import load_iris
iris = load_iris ()

# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.4, random_state=1)

# printing the shapes of the new X objects
print (X_train.shape)
print (X_test.shape)

# printing the shapes of the new y objects
print (y_train.shape)
print (y_test.shape)

# Given below uses KNN (K nearest neighbors) classifier
# load the iris dataset as an example

from sklearn.datasets import load_iris
iris = load_iris ()

# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.4, random_state=1)

# training the model on training set
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier (n_neighbors=3)
knn.fit (X_train, y_train)

# making predictions on the testing set
y_pred = knn.predict (X_test)

# comparing actual response values (y_test) with predicted response values (y_pred)
from sklearn import metrics
print ("kNN model accuracy:", metrics.accuracy_score (y_test, y_pred))

# making prediction for out of sample data
sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
preds = knn.predict (sample)
pred_species = [iris.target_names[p] for p in preds]
print ("Predictions:", pred_species)

# saving the model
from sklearn.externals import joblib
joblib.dump (knn, 'iris_knn.pkl')
