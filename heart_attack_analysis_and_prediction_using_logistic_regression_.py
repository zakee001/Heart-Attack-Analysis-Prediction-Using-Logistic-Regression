# -*- coding: utf-8 -*-
"""Heart Attack Analysis and Prediction Using Logistic Regression .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19uiEHyrVra7idacwx70UpqTxrBGWT5wW
"""

#importing libraries 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

#reading the csv file
df = pd.read_csv("heart.csv")

#Viewing the data
df.head()

#converting the values into x and y
x = df.iloc[:,0:13].values
y = df.iloc[:,13].values

#converting the data into test/train split
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2 ,random_state =0)

#fit-transform the data 
from sklearn.preprocessing import StandardScaler
s = StandardScaler()
x_train = s.fit_transform(x_train)
x_test = s.fit_transform(x_test)

#Using Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)

#printing the 
y_pred =classifier.predict(x_test)
y_pred

#print the accuracy score.
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
print(accuracy_score(y_test,y_pred))

#printing the y-predicted vs y_actual
ent1 = pd.DataFrame(y_test)
ent2 = pd.DataFrame(y_pred)
  
# concatenating the DataFrames
det = pd.concat([ent1,ent2], join = 'outer', axis = 1)
  
# displaying the DataFrame
print(det)

