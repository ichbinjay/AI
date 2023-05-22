import numpy as np

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn import datasets

from sklearn import metrics

import matplotlib.pyplot as plt

bc=datasets.load_breast_cancer()

'''X=slf.iloc[:100, :-1].values

y=slf.iloc[:100, -1].values'''

X = bc.data[:100]

y = bc.target[:100]

from sklearn import preprocessing

  

# label_encoder object knows how to understand word labels.

label_encoder = preprocessing.LabelEncoder()

  

# Encode labels in column 'species'.

y= label_encoder.fit_transform(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

from sklearn import tree

dtc=tree.DecisionTreeClassifier()

dtc.fit(X_train,y_train)

y_pred_dtc=dtc.predict(X_test)

acc_dtc=metrics.accuracy_score(y_test,y_pred_dtc)

pre_dtc=metrics.precision_score(y_test,y_pred_dtc)

reca_dtc=metrics.recall_score(y_test,y_pred_dtc)

f1score_dtc=metrics.f1_score(y_test,y_pred_dtc)

fig, ax = plt.subplots(figsize=(20, 10))

tree.plot_tree(dtc, ax=ax)

plt.show()



clf = MLPClassifier(hidden_layer_sizes=(20,10),

                    random_state=5,

                    learning_rate_init=0.01)

# Fit data onto the model

clf.fit(X_train_std,y_train)

ypred_mlp=clf.predict(X_test_std)

accuracies["mlp"]=metrics.accuracy_score(y_test, ypred_mlp)

precisions["mlp"]=metrics.precision_score(y_test, ypred_mlp, average='weighted')

recalls["mlp"]=metrics.recall_score(y_test, ypred_mlp, average='weighted')

f1scores["mlp"]=metrics.f1_score(y_test, ypred_mlp, average='weighted')

print(accuracies["mlp"], precisions["mlp"], recalls["mlp"], f1scores["mlp"])
