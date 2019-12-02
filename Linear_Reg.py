import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

print(data.head())


predict = "G3"

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size = 0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
acrc = linear.score(x_test, y_test)

print(acrc)

print("mx: \n", linear.coef_)
print("Y-intcpt: \n", linear.intercept_)

predictions = linear.predict(x_test)

for i in range(len(predictions)):
    print(predictions[i], x_test[i], y_test[i])



