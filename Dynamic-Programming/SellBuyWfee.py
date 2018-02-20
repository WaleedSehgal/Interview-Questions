# -*- coding: utf-8 -*-
"""
@author: Waleed

Calculate best time to sell and buy stocks with a transaction fee with every transaction.
"""

profit = 0
buy = -(prices[0])
        
for i in range(1,len(prices)):
            
    profit = max(profit, ns+prices[i]-fee)
    buy = max(ns, profit-prices[i])

return profit
