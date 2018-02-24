# -*- coding: utf-8 -*-
"""
@author: Waleed

Add two numbers represented by two linkedlists and return a linkedlist representing the Sum number.
"""

class Node(object):
    def __init__(self,data=None, next_node=None):
        self.data=data
        self.next_node=next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
    
    def __str__(self):
        return self.get_data()                

class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
        
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    def addTwo(self, l1, l2):
        
        a,b,c = 0,0,0
        
        sl = LinkedList()
                
        while l1!=None or l2!=None:
            
            if l1==None:
                a=0
            else:
                a = l1.data
                
            if l2==None:
                b=0
            else:
                b = l2.data
            
            Sum = a+b+c
            
            
            if Sum>=10:
                c = 1
                Sum = Sum%10
            else:
                c=0
                        
            sl.insert(Sum)
            
            if l1!=None:
                l1 = l1.next_node
            
            if l2!=None:
                l2 = l2.next_node
        
        if c>0:
            sl.insert(c)
        
        return sl
            
    def show(self):
        
        current = self.head
        print('head-', end='')
        while current:
            print('-->', end='')
            print(current.get_data(), end='')
            current = current.get_next()

l1 = LinkedList()
l2 = LinkedList()

l1.insert(1)
l1.insert(1)
l1.insert(9)

l2.insert(1)
l2.insert(0)
l2.insert(1)

ll = LinkedList()
sl = ll.addTwo(l1.head,l2.head)
sl.show()
