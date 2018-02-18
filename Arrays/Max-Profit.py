# -*- coding: utf-8 -*-
"""
@author: Waleed
"""

a = [7,1,5,3,6,4]

buy = a[0]
sell,profit = 0,0

for i in range(len(a)):
    if a[i]<buy:
        buy = a[i]
    else:
        p = a[i]-buy
        if p>profit:
            sell = a[i]
            profit = p

print('Buy:', buy)
print('Sell:', sell)
print('Profit:',profit)
