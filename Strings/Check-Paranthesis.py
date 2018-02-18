# -*- coding: utf-8 -*-
"""
@author: Waleed
"""

def paranthesis(a):

    n = len(a)
    
    dct = {'(':')', '[':']', '{':'}'}
    
    if n==0 or n%2!=0:
        return False 

    queue = list()
    
    i=0
    while i<len(a):
        
        if len(queue)==0:
            queue.append(a[i])
            i+=1
            
        elif len(queue)!=0 and dct.get(queue[-1])==a[i]:
            queue.pop()
            i+=1
        
        elif len(queue)!=0 and dct.get(queue[-1])!=a[i]:
            queue.append(a[i])
            i+=1

    if len(queue)==0:
         print('Inorder!')
         return True 
    else:
         print('Out of Order!')
         return False
     
a = ['{','(',')','}']

paranthesis(a)
