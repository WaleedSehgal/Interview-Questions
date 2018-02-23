# -*- coding: utf-8 -*-
"""
@author: Waleed

generate a valid string of all possible combinations of n sets of parenthesis.
"""

def generatePar(n):
    
    if n==0:
        return None
    
    return generateparHelp('', n, 0)


def generateparHelp(curr,popen, pclose):
    
    if popen==0:
        
        return [curr+')'*pclose]
    
    if pclose==0:
        
        return generateparHelp(curr+'(', popen-1, pclose+1)
    
    return generateparHelp(curr+'(', popen-1, pclose+1) + generateparHelp(curr+')', popen, pclose-1)

print(generatePar(3))
