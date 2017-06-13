import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools as it
import time
from sys import argv
from networkx.algorithms import isomorphism

adjList = {0: set([1,2]), 1: set([0,2,3]), 2: set([0,1,3,4]), 3: set([1,2,4,5]), 4: set([2,3,5]), 5: set([3,4])}
G = nx.Graph()
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_edge(0,1)
G.add_edge(0,2)

G.add_edge(1,0)
G.add_edge(1,2)
G.add_edge(1,3)

G.add_edge(2,0)
G.add_edge(2,1)
G.add_edge(2,3)
G.add_edge(2,4)

G.add_edge(3,1)
G.add_edge(3,2)
G.add_edge(3,4)
G.add_edge(3,5)

G.add_edge(4,2)
G.add_edge(4,3)
G.add_edge(4,5)

G.add_edge(5,3)
G.add_edge(5,4)

pos = nx.circular_layout(G)
nx.draw(G,pos)
nx.draw_networkx_labels(G,pos)

def dfs_paths_onlyadj(graph, start, goal):
   stack = [(start, [start])]
   while stack:
      (vertex, path) = stack.pop()
      for k in graph[vertex] - set(path):
         if k == goal or len(path) == 3:
            yield path + [k]
         else:
            stack.append((k, path + [k]))
def dfs_paths(graph, start, goal):
   stack = [(start, [start])]
   while stack:
      (vertex, path) = stack.pop()
      for k in graph[vertex] - set(path):
         if k == goal:
            yield path + [k]
         else:
            stack.append((k, path + [k]))

print list(dfs_paths(adjList,0,5))
print "\n"
print list(dfs_paths_onlyadj(adjList,0,5))

#graph = adjList 
#start = 0
#goal = 5
#stack = [(start, [start])]
#print stack
#while stack:
#   print "stack is ...  ", stack
#   (vertex, path) = stack.pop()
#   print "top of stack is poped, (vertex, path) ...  ", (vertex, path)
#   print "goes to for loop of neighbors"
#   for k in graph[vertex] - set(path):
#      "print neighbor not in path is ...  ", k
#      if k == goal:
#         print "neighbor is goal! path + [k] ...  " , path + [k]
#      else:
#         print "neighbor is not goal! appending to stack (k, path + [k])"
#         stack.append((k, path + [k]))
#   print "\n"

