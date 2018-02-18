# -*- coding: utf-8 -*-
"""
@author: Waleed
"""

s = 'babadada'
 
check = list()
idx = {}
pdr = list()


for i, c in enumerate(s):
   
    if c in check:
        for c in sorted(idx):
            a = s[idx[c]:i+1]
            b = ''.join(reversed(a))
            if a==b:
                pdr.append(a)
    check.append(c)    
    idx[c] = i
   
    
pdr.extend(idx.keys())

if not pdr:
    r = ''
else:
    r = max(pdr, key = len)
    print(r)

