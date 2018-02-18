# -*- coding: utf-8 -*-
"""
@author: Waleed
"""

def grading(grades):
    
    results = list()
    
    for i in range(0,len(grades)):
        
        if grades[i]==100:
            results.append(grades[i])
            
        elif grades[i]<=38:
            results.append(grades[i])
        else:
            c = grades[i]/10
            c = int(c)
            cap1 = c*10+5
            cap2 = c*10+10
            
            a =  cap1-grades[i]
            b = cap2-grades[i]
            
            if grades[i]<cap1 and a<3:
                results.append(cap1)
            elif grades[i]>cap1 and grades[i]<cap2 and b<3:
                results.append(cap2)
            else:
                results.append(grades[i])
    print(grades)        
    print(results)
    return results
            
            
grades = [29, 43, 100, 88, 53, 96, 77, 75, 66, 42, 91, 33, 0]            
            
grading(grades)            
