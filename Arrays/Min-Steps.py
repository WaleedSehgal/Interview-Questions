# -*- coding: utf-8 -*-
"""
@author: Waleed
"""

a = [10,9,8,7,6,5,1,3,5,67]

def stepcost(a):
      n  =len(a)
      
      if n==0 or n==1:
            return 0
        
      m_a, m_b  = a[0], a[1]
        
      for i in range(2,n):
            m_a,m_b = m_b, min(m_a,m_b)+a[i]
            
      return min(m_a,m_b)
        
        
stepcost(a)
            
        
        
