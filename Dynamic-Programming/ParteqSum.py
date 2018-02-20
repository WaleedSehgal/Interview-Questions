"""
@author: Waleed

Check wether a given array can be partitioned into two arrays of equal sums.
"""

arr = [1,2,3,4,5,6,7]
    
target = sum(arr)/2

sums = {0}

#store sums of all subsets for each i in arr
for i in range(len(arr)):
    sums.update({(j+arr[i]) for j in sums})

if target in sums:
    print('Yes')
else:
    print('No')
