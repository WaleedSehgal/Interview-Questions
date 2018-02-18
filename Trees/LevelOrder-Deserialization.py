# -*- coding: utf-8 -*-
"""
@author: Waleed
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
    
    def deserialize(self,arr):
        
        if len(arr)==0:
            return None
        
        if len(arr)==1:
            self.root=Node(arr[0])
        
        self.deserializerec(arr,0)
        
        return self.root
        
    def deserializerec(self, arr, i):
        
        if i>=len(arr):
            return None
        
        elif i<len(arr):
            
            if arr[i]==-1:
                return None
            
            node = Node(arr[i])
           
            if i==0:
                self.root = node
            
            l = (2*i) +1
            r = (2*i) +2
            
            node.lchild = self.deserializerec(arr, l)
            node.rchild = self.deserializerec(arr, r)
            
        return node
        
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
                              
arr = [40,30,48,15,-1,45,50,10,20]

Tree = BSTree()
root= Tree.deserialize(arr) 
Tree.inLevel(Tree.root)

        
