# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 03:38:58 2018

Given two integers as strings return their product without converting string to int directly, eg: int('12').
@author: Waleed
"""
num1 = '110'
num2 = '110'

d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
n1 = 0
n2 = 0
        
l1 = len(num1)-1
l2 = len(num2)-1
        
for i in range(len(num1)):
  num = num1[i]
  n1 += d[num]*(10**(l1))
  l1-=1

for j in range(len(num2)):
    num = num2[j]
    n2 += d[num]*(10**(l2))
    l2-=1

product = n1*n2

print(str(product))  
