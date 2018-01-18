import pandas as pd
from sklearn import metrics
import numpy as np
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn import tree
import pydot

dataset = pd.read_csv('eng_survey_trees.csv')
CV =  dataset.program.reshape((len(dataset.program), 1))
classes = []
for i in CV:
	if i not in classes:
		classes.append(i[0])
for i in dataset:
	if (i!='program'):
		number = LabelEncoder()
		dataset[i] = number.fit_transform(dataset[i].astype('str'))
data = (dataset.ix[:,'field_interest':'gender'].values).reshape((len(dataset.program), 19))

model= RandomForestClassifier(n_estimators=100, random_state=1, criterion="entropy", max_features=17, min_samples_leaf =2, max_depth=4)
model.fit(data, CV.ravel())
predicted = model.predict(data)
print(metrics.confusion_matrix(CV, predicted, labels=classes))
print("Accuracy of the model: with random forest RF", model.score(data,CV.ravel()))
print "RF # of classes", model.n_classes_
print "RF # of features used", model.n_features_

skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=True)
X = data
y = CV.ravel()
scores = []
for train_index, test_index in skf.split(X, y):
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]
	model.fit(X_train, y_train)	
	scores.append(model.score(X_test,y_test))
overall_score = 0
for strat_score in scores:
	overall_score += strat_score
print("MSE of every fold in 5 stratified fold cross validation RF: ", scores)
print("Mean of the 5 stratified fold cross-validation RF: ", overall_score/5)

print "RF feature importances"
print model.feature_importances_, 
# # Create linear regression object
# #
print ""
DT = DecisionTreeClassifier(random_state=1, criterion="entropy", max_features=17, min_samples_leaf=2, max_depth=4)

# # Train the model using the training sets
DT.fit(data, CV.ravel())
print "DT feature importances"
print DT.feature_importances_
tree.export_graphviz(DT, out_file='tree.dot')


print("Accuracy score for the model: DT \n", DT.score(data,CV.ravel()))
model = DecisionTreeClassifier()

kf = StratifiedKFold(n_splits=5, random_state=None, shuffle=True)
X = data
y = CV.ravel()
scores = []
for train_index, test_index in skf.split(X, y):
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]
	model.fit(X_train, y_train)	
	scores.append(model.score(X_test,y_test))
overall_score = 0
for strat_score in scores:
	overall_score += strat_score
print("MSE of every fold in 5 stratified fold cross validation DT: ", scores)
print("Mean of the 5 stratified fold cross-validation DT: ", overall_score/5)

predicted = DT.predict(data)
print(metrics.confusion_matrix(CV, predicted, labels=classes))
# print classes





