# -*- coding: utf-8 -*-
"""
@author: Waleed

Find a path from given start node to end node in a graph using BFS technique.
"""
from collections import deque
         
graph = { 'a': ['b','c'],
          'b': ['f'],
          'c': ['d'],
          'd': ['e'],
          'e': [],
          'f': []
        }

def graphPathBFS(graph, start, end):
    
    todo = [(start, [start])]
    
    while len(todo):
        
        node, path = todo.pop(0)
        print(node)
        for n in graph[node]:
            
            if n in path:
                continue
            
            elif n==end:
                return path+[n]
            
            else:
                todo.append((n, path+[n]))
    
print(graphPathBFS(graph, 'a', 'e'))
