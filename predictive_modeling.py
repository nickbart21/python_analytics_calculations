import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier

df = pd.read_csv(r'breast_cancer_ds.csv')

# Initial data exploration
pd.set_option('display.max_columns', None)
print(df.head())

print(df.describe())

dfIsNull = df.isnull().sum(axis= 0)
print(dfIsNull)

print(df.corr())

#correlation plot
plt.matshow(df.corr())
plt.title('Correlation Matrix', position = (0.5, 1.1))
plt.colorbar()
plt.xticks(range(10),list(df.columns))
plt.yticks(range(10), list(df.columns))
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.xticks(rotation=90)
plt.show()

#Logistic regression ---- Convergence problem

X = df.iloc[:, 0 : 8]
Y = df.Classification

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=34)
lr = linear_model.LogisticRegression()

lr.fit(X_train, Y_train)
print('\n Logistic Regression Coefficients\n', lr.coef_)

lr_train_pred = lr.predict(X_train)
lr_test_pred = lr.predict(X_test)

trainAC = metrics.accuracy_score(Y_train, lr_train_pred)
testAC =  metrics.accuracy_score(Y_test, lr_test_pred)

print('\n Logistic Regression Accuracy Score\n', testAC)

LRtrain_cm = metrics.confusion_matrix(Y_train, lr_train_pred)
print('\n Train Confusion Matrix\n', LRtrain_cm)

LRtest_cm = metrics.confusion_matrix(Y_test, lr_test_pred)
print('\n Test Confusion Matrix\n', LRtest_cm)

plt.figure()
plt.matshow(LRtest_cm)
plt.title('LR Confusion Matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted Label')

#------------Part 3--------------------------------

print('--------- Part 3 ----------------')

print('\n\n Naive Bayes\n')

NB = GaussianNB()

NB.fit(X_train, Y_train)

NB_train_pred = NB.predict(X_train)
NB_test_pred = NB.predict(X_test)

print('\n Naive Bayes Train Accuracy Score\n', metrics.accuracy_score(Y_train, NB_train_pred))

print('\n Naive Bayes Test Accuracy Score\n', metrics.accuracy_score(Y_test, NB_test_pred))

NBtrain_cm = metrics.confusion_matrix(Y_train, NB_train_pred)
print('\n Train Confusion Matrix\n', NBtrain_cm)

NBtest_cm = metrics.confusion_matrix(Y_test, NB_test_pred)
print('\n Test Confusion Matrix\n', NBtest_cm)

np.set_printoptions(precision=2)
print('\n Probability for correctly predicting the label\n', NB.predict_proba(X_test[:5]))

#------------Part 4--------------------------------

print('--------- Part 4 ----------------')

print('\n\n Decision Tree\n')

DT = tree.DecisionTreeClassifier(max_depth=3, min_samples_split=5)

DT.fit(X_train, Y_train)

DT_pred = DT.predict(X_test)

print('\n Decision Tree Accuracy Score\n', metrics.accuracy_score(DT_pred, Y_test))

print('\n Classification Report\n', metrics.classification_report(Y_test, DT_pred))

DT.feature_importances_

print('\n Feature Importances\n', pd.DataFrame({'variable':df.columns[:8], 'importance':DT.feature_importances_}))

#------------Part 5-------------------------------- Convergence Issue

print('--------- Part 5 ----------------')

print('\n\n Neural Network\n')

scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

NN = MLPClassifier(solver = 'lbfgs', alpha = 1e-5, hidden_layer_sizes = (10,4), random_state = 1)

NN.fit(X_train_scaled, Y_train)

NN_pred = NN.predict(X_test_scaled)

print('\n Neural Network Accuracy Score\n', metrics.accuracy_score(NN_pred, Y_test))

print('\n Classification Report\n', metrics.classification_report(Y_test, NN_pred))

#------------Part 6--------------------------------

print('--------- Part 6 ----------------')

print('The Neural Network was the best model with an Accuracy Score of .8')

print('According to the Decision Tree feature importances, Glucose is the most imoprtant feature.')
