# -*- coding: utf-8 -*-
"""
@author: Waleed
"""  

nums = [-1,1,0,2,3,-1]
nums = sorted(nums)
result = list()
n = len(nums)

for i in range(n-1):
            
    left = i+1
    right = n-1
            
    if i>0 and nums[i]==nums[i-1]:
       continue
                
    while left<right:
                
       s = nums[i]+nums[left]+nums[right]
                
       if s<0:
          left+=1
                
       elif s>0:
          right-=1
                
       else:
          result.append([nums[i],nums[left],nums[right]])
                    
          while left<right and nums[left]==nums[left+1]:
             left+=1
          while left<right and nums[right]==nums[right-1]:
             right-=1
                    
       left+=1
       right-=1

return result
        
