# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 14:35:40 2018

@author: Hanan
"""
import pandas as pd
       ##########Data###########
training_data = pd.read_csv('trainingdata.txt', sep="," ,names=["timeCharged" ,"batteryLasted"])

X = training_data.iloc[:,:-1]
Y = training_data.iloc[:,-1]

###############analyzing data#############
import matplotlib.pyplot as plt

#plt.plot(X,Y,'.')

    ##########the data is completely linear (until the battery is fully charged)
    #when the battery is charged more than or equal 4 hours(fully charged)
    #it lasts about 8 hours
updataded_X=X[Y!=8]
updated_Y = Y[Y!=8]
#plt.plot(updataded_X,updated_Y,'.')


    ###model###
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(updataded_X,updated_Y)    #training on data that battery is charged below or equal 4 hours

##########make predictions######3
x_pred = float(input())
if x_pred >4.0:    #in case that battery is charged more than 4 hours
    print(8.0)
else:
    print(round(model.predict(x_pred)[0],2))