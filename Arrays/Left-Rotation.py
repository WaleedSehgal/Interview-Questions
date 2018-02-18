# -*- coding: utf-8 -*-
"""
@author: Waleed
"""

a = [1,2,3,5,6,7,8]
leftrot = 3

i = 0
while i<leftrot:
    r = a[0]
    a.remove(r)
    a.append(r)
    i+=1

print(a)
