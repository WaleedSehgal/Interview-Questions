# -*- coding: utf-8 -*-
"""
@author: Waleed
Find the substring in the string and return index of first character's occurence.
"""

s = 'Find the substring in this string'
ss = 'the sub'

ssl = len(ss)

found  = False

for i,c in enumerate(s):
    
    if c == ss[0]:
        sub = s[i:i+ssl] 
        if sub==ss:
            print(i)
            break
if found!=True:
           print('substring not in string')

