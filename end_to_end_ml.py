# -*- coding: utf-8 -*-
"""end-to-end-ml.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16PkqePjklPz972FZI51UVKhghU_UvDQO
"""

import numpy as np
import pandas as pd

df=pd.read_csv('/content/placement.csv')

df.head()

df.shape

df.info()

df=df.iloc[:,1:]

df.head()

import matplotlib.pyplot as plt

plt.scatter(df['cgpa'],df['iq'],c=df['placement'])

X=df.iloc[:,0:2]
y=df.iloc[:,-1]

X.shape

y.shape

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1)

X_train

y_train

X_test

y_test

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

X_train=sc.fit_transform(X_train)

X_train

X_test=sc.transform(X_test)

X_test

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()

#model training
lr.fit(X_train,y_train)

y_pred=lr.predict(X_test)

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

from mlxtend.plotting import plot_decision_regions

plot_decision_regions(X_train,y_train.values,clf=lr,legend=2)

import pickle

pickle.dump(lr,open('model.pkl','wb'))
