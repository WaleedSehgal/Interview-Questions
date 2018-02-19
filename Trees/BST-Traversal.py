# -*- coding: utf-8 -*-
"""
@author: Waleed
"""

from collections import deque

class Node(object):
    
    def __init__(self,val,isroot=None,lchild=None,rchild=None):
        self.val=val
        self.lchild=lchild
        self.rchild=rchild
        self.isroot=isroot
        
    def set_lchild(self,lchild):
        
        if self.lchild==None:
            self.lchild=lchild
        
    def set_rchild(self,rchild):
        
        if self.rchild==None:
            self.rchild=rchild
    
    def __str__(self):
        return str(self.val)
        
class Tree(object):
    
    def __init__(self):
        self.root=None
    
    #Add node to BST
    def add(self,n):
        if self.root==None:
            self.root=Node(n,isroot=True)
        else:
            self.add_node(self.root,n)
    
    #add_node helper    
    def add_node(self,current,n):
            
        if current.val<n:
                if current.rchild:
                    self.add_node(current.rchild,n)
                else:
                    current.rchild=Node(n)
        else:
                if current.lchild:
                    self.add_node(current.lchild,n)
                else:
                    current.lchild=Node(n)
    
    #In Order Traversal
    def inOrder(self,root):
        
        if root:
            self.inOrder(root.lchild)
            print(root.val, end=' ')
            print('\n')
            self.inOrder(root.rchild)
    
    #Pre Order Traversal
    def preOrder(self,root):
        
        if root:
            print(root.val, end=' ')
            self.preOrder(root.lchild)
            self.preOrder(root.rchild)
        
    #Post Order Traversal    
    def postOrder(self,root):
        
        if root:
            self.postOrder(root.lchild)
            self.postOrder(root.rchild)
            print(root.val, end='--')
    
   
    #Level Order Traversal        
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


#Create a BST instance         
t1 = Tree()

t1.add('g')
t1.add('b')
t1.add('i')
t1.add('a')
t1.add('c')
t1.add('h')
t1.add('j')
t1.add('f')
t1.add('k')

t1.inLevel(t1.root)

