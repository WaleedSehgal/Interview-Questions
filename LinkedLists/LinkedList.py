# -*- coding: utf-8 -*-
"""
@author: Waleed

Contains functions for linkedlist insertion, printing a linkedlist, returning size of a linkedlist.
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
                

class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
        
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count+=1
            current = current.get_next()
        return count
    
   def show(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()
            
       

llist = LinkedList()
llist.insert(5)
llist.insert(4)
llist.insert(3)
llist.insert(2)
llist.insert(1)


llist.show()
print(llist.size())
