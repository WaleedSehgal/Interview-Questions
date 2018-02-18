# -*- coding: utf-8 -*-
"""
@author: Waleed
"""

a = [0,0,0,0,1]
b = [1,0,0,0,0]

l1 = len(a)
l2 = len(b)

mx = 0

check = [[0 for x in range(l2+1)] for y in range(l1+1)]

for i in range(l1):
   for j in range(l2):
        
        if a[i]==b[j]:
            
            check[i][j]=check[i-1][j-1]+1
            #print(check[i-1][j-1])
            if check[i][j]>mx:
                mx = check[i][j]
            
        else:
            check[i][j]=0
            

print(mx)
