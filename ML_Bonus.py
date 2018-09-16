# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:07:14 2018

@author: Lenovo
"""

######
N = int(input())  # number of elements

numbers = input().split(" ")

numbers=[float(i) for i in numbers]
    
     ###mean###
mean = sum(numbers) /N

     ####median####
numbers.sort()
median =0
if N%2 ==0:
    mid = int(N/2)
    median = (numbers[mid-1]+numbers[mid])/2
else:
    mid =int((N-1)/2)
    median = numbers[mid]
    
    #####mode#######
from collections import Counter
count = Counter()   # Make dictionary of each unique number in list (as key ) 
                    #and its occurrence in list (as value)    
for item in numbers:
    count[item]+=1    #{number: no_of_occurence , }
    
import operator
     #sort according to values(number of occurrence of each unique number)#
sorted_count = sorted(count.items(), key=operator.itemgetter(0)) #return #list of tuples sorted by the second element in each tuple (value)
         
max_count = sorted_count[0][1]   #maximum occurrence
smallest= sorted_count[0][0]     #number that has maximum occurrence
for number , count in sorted_count[1:]:
    
    if count == max_count:
        if number <smallest:
            smallest = number
mode = smallest            #the smallest number of numbers that has the maximum occurrence
if(mode%1 ==0):   #means its integer number 1.0 != 1
    mode = int(mode)
       #or#
    #######simple way########
#from scipy import stats
#mode = stats.mode(numbers)[0][0]
#if(mode%1 ==0):   #means its integer number 1.0 != 1
#    mode = int(mode)
       ################standard deviation#############
import numpy as np
numbers = np.array(numbers)   #convert from list to numby array to facilite math operations

std = np.sqrt( np.sum( (numbers-mean)**2 ) /N  )


#########Lower and Upper Boundary of the 95% Confidence Interval for the mean########

margin_of_error =1.96 *(std/np.sqrt(N))   #for .95 confidence

lower = mean -margin_of_error
upper = mean + margin_of_error

##########################################
from scipy import stats
mode = stats.mode(numbers)[0][0]
if(mode%1 ==0):   #means its integer number 1.0 != 1
    mode = int(mode)
print(round(mean,1))
print(round(median,1))
print(mode)
print(round(std,1))
print(round(lower,1) , round(upper,1))


    


 