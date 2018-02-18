# -*- coding: utf-8 -*-
"""
@author: Waleed
"""


def lettComb(digits):
        d2a = { '1': '',    '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs','8': 'tuv', '9': 'wxyz',
        '0': ' '}
        ans = [''] if digits else []
        
        for d in digits:
            n_ans = list()
            for e in d2a[d]:
                for r in ans:
                    n_ans.append(r+e)
                    
            ans = n_ans  
        
        print(ans)
        return ans
    
lettComb('2356')
