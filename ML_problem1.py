# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:11:58 2018

@author: Hanan
"""
import pandas as pd

############take inputs from user#####
   #1#
F_train , N_train =input().split()  #F_train:no.of features
                                            #N_train : no of rows in training data
   ##2# ######input training data##########
lines = []       
for i in range(int(N_train)):
     row= input().split()
     lines.append(row)
   #3#

N_pred =float(input())   #no.of samples for predictions
    #4####features for prediction##
lines2 = []       
for i in range(int(N_pred)):
         row= input().split()
         lines2.append(row)
################DATA###########################
def toFloat(x):
    return pd.to_numeric(x)  #convert string values of series "x" to float values

train_data=pd.DataFrame(lines)  #train
train_data=train_data.apply(toFloat,axis=1) #convert data from string to float

X_pred=pd.DataFrame(lines2).apply(toFloat,axis=1)  #predict the price (y) for each row
####################Preprocessing##############333
     #polynomial features#####
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X_train =train_data.iloc[:,:-1]
Y_train = train_data.iloc[:,-1]

poly = PolynomialFeatures(degree=3)   

poly_features = poly.fit_transform(X_train)   #polynomial features for training
X_pred_poly =   poly.fit_transform(X_pred)

      #####model######
model = LinearRegression()
model.fit(poly_features ,Y_train)  #training the model

     #make predictions#####
#print(X_pred)

predictions = model.predict(X_pred_poly)
for i in predictions:
    print(i)

