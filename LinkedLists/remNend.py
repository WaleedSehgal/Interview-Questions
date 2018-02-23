# -*- coding: utf-8 -*-
"""
@author: Waleed

Removes nth node from the end of a linked list and returns head.
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
    
    def trav(self, head, n):
        
        a = head
        b = head
       
        if head.get_next()==None and n==1:
            return None
        
        if head.next_node.get_next()==None and n==2:
            return head.get_next()
        
        i=1
        
        while b.get_next():
            
            if i<n+1:
                b = b.get_next()
                i+=1
             
            else:
                a = a.get_next()
                b = b.get_next()
        
        if i==n:
            return head.get_next()
        else:    
            a.set_next(a.next_node.get_next())   
            return head

llist = LinkedList()
llist.insert('5')
llist.insert('4')
llist.insert('3')
llist.insert('2')
llist.insert('1')


print(llist.trav(llist.head,5))



