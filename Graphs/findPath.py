# -*- coding: utf-8 -*-
"""
@author: Waleed

returns a path in a graph, if their exists one from the given start node to the end node.
"""

graph = {'a':['b'],
         'b':['a','c'],
         'c':['c','d'],
         'd':['b']
         }

def findpath(graph, start, end, path=[]):
    
    path.extend(start)
    
    if start==end:
        return path
    
    if start not in graph.keys():
        path.pop() 
        return 
    
    for node in graph[start]:
        
        if node not in path:
            p = findpath(graph, node, end, path)   
            if p:
                return p
    return 'No path found'

print(findpath(graph, 'a', 'd', path=[]))
print(findpath(graph, 'd', 'a', path=[]))
