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
    
    #Add node helper    
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
    #Returns Height of a BST
    def height(self,root):
        h=miscFuncs()
        he = h.heighthelp(root)
        return he
        

class miscFuncs(object):
    
    #Height helper
    def heighthelp(self,n):
        
        if n is None:
            return 0
        else:
            
            lheight=self.heighthelp(n.lchild)
            rheight=self.heighthelp(n.rchild)
            
            if lheight>rheight:
                return lheight+1
            else:
                return rheight+1
    
    #Find if two BSTs are identical
    def identical(self, root1, root2):
        if root1==None and root2==None:
            return True
        elif root1==None or root2==None:
            return False
        
        return root1.val==root2.val and self.identical(root1.lchild,root2.lchild) and self.identical(root1.rchild, root2.rchild)             
                
    #returns number of nodes of a BST
    def size(self,root):
        if root==None:
            return 0
        
        lsize=self.size(root.lchild)
        rsize=self.size(root.rchild)
        
        return lsize+rsize+1
    
    #Checks if a Tree is a BST
    def isbst(self,root, minval,maxval):
        
        if root==None:
            return True
        
        if root.val<=minval or root.val>maxval:
            return False
        
        return  self.isbst(root.lchild, minval, root.val) and self.isbst(root.rchild,root.val,maxval)     
    
            
#Create a BST instance         
t1 = Tree()
t2 = Tree()
t3 = Tree()

#t1
t1.add('g')
t1.add('b')
t1.add('i')
t1.add('a')
t1.add('c')
t1.add('h')
t1.add('j')
t1.add('f')
t1.add('k')

#t2
t2.add('g')
t2.add('b')
t2.add('i')
t2.add('a')
t2.add('c')
t2.add('h')
t2.add('j')
t2.add('f')
t2.add('k')

#t3
t3.add(10)
t3.add(4)
t3.add(6)
t3.add(1)
t3.add(3)

check = miscFuncs()


print('t1s height is: ',t1.height(t1.root))

print('t1s size: ',check.size(t1.root))

print('Are t1 & t2 identical: ',check.identical(t1.root, t2.root))

#function needs initial arbitrary min and max limits 
#in python2 it was possible to set it to min and max integer value
print('Is t1 a BST? ',check.isbst(t3.root, -1, 10**5))

