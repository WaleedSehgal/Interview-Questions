# -*- coding: utf-8 -*-
"""
@author: Waleed
Deserializes a tree from an array constructed through pre-order serialization. 
"""

from collections import deque

class Node(object):
    
    def __init__(self, val, lchild = None, rchild = None):
        
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
        
    def __str__(self):
        return str(self.val)
    
class BSTree(object):
    
    def __init__(self):
        
        self.root = None
    
    def deserialize(self, arr):
        
        que = deque()
        
        for i in range(len(arr)):
            que.append(arr[i])
        
        root = self.POdeserialize(que)
        
        return root
    
    def POdeserialize(self, que):   
        
        if len(que)==0:
            return None
        
        if len(que)==1:
            return Node(que[0])
        
        current = Node(que.popleft())
       
        currque = deque()
        
        while len(que)!=0 and que[0]<current.val:
            currque.appendleft(que.popleft())
            
        current.lchild = self.POdeserialize(currque)
        current.rchild = self.POdeserialize(que)
        
        return current
          
            
    def inLevel(self,root):
        q = deque()
        if root==None:
            return None
        
        if root:
            q.append(root)
            q.append(None)
            
            while q:
                current = q.popleft()
                
                if current==None and len(q)>0:
                    q.append(None)
                    print('')
            
                elif current!=None:  
                    
                    if current.lchild:
                        q.append(current.lchild)
                    if current.rchild:
                        q.append(current.rchild)
                    
                    print(current, end=' ')
            
        
        
POarray = [10,5,1,7,40,30,50,45]

bst = BSTree()

root = bst.deserialize(POarray)

bst.inLevel(root)
