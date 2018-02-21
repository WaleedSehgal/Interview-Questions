# -*- coding: utf-8 -*-
"""
@author: Waleed

Find a path from given start node to end node in a graph using BFS technique.
"""
from collections import deque

graph = {'a':['b'],
         'b':['c','d'],
         'c':['d'],
         'd':['e'],
         'e':['f']
         }
         
def bfs(graph, start, end):
    
    #maintain a list of already visited nodes 
    visited = []
    
    
    queue = deque()
    queue.appendleft([start])
    
    while queue:
        
        #use last element from path in queue to explore nodes
        pathIn = queue.popleft()
        node = pathIn[-1]
        
        #only explore connections for nodes that hasnt been visited yet
        if node not in visited:
            connections = graph[node]
            
            #check each connection node of the current node
            for connection in connections:
                path = list(pathIn)
                path.extend(connection)
                queue.append(path)
                
                if connection==end:
                    return path
            
            visited.append(node)
            
    
print(bfs(graph,'a','f'))
