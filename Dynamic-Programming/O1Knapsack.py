# -*- coding: utf-8 -*-
"""
@author: Waleed
"""

cap = 50
value = [200,300,50,120]
weight = [10,50,20,30]
n = len(weight)

valmax = [[None for x in range(cap+1)] for y in range(n+1)]

def KnapSack(n, cap):
    
    if valmax[n][cap]!=None:
        return valmax[n][cap]
    
    if n==0 or cap==0:
        return 0
    
    elif weight[n-1]>cap:
        result = KnapSack(n-1, cap)
    
    else:
        
        t1 = KnapSack(n-1,cap)
        t2 = value[n-1] + KnapSack(n-1, cap-weight[n-1])
        result = max(t1,t2)
        
    valmax[n][cap] = result
    return result        


print(KnapSack(n,cap))
