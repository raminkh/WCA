#for the case of this graph and for n = 4, e = 3, they don't match (dfs method is correct as opposed to realization combination)
#it hasn't been checked for optimization in terms of time yet
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools as it
import time
from sys import argv
from networkx.algorithms import isomorphism
from pandas import *

adjList = {0: [1,2], 1: [0,2,3], 2: [0,1,3,4], 3: [1,2,4,5], 4: [2,3,5], 5: [3,4]}
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

def dfs_paths(graph, root, target, path=None):
   if path is None:
      path = [root]

   if root == target:
      yield path

   for vertex in [x for x in graph[root] if x not in path]:
      for each_path in dfs_paths(graph,vertex,target,path+[vertex]):
         yield each_path

nodes = G.nodes()
linked_node_num = 4
all_paths = []
for i in range(len(nodes)):
   for j in range(len(nodes)):
      paths = list(dfs_paths(adjList, i, j))
      index = []
      for k in range(len(paths)):
         if len(paths[k]) < linked_node_num:
            index.append(k)
         else:
            paths[k] = paths[k][:linked_node_num]
      paths = [l for m, l in enumerate(paths) if m not in index]
      all_paths.append(paths)

all_paths = sum(all_paths,[])
for i in range(len(all_paths)):
   sublist = all_paths[i]
   sublist = sorted(sublist)
   all_paths[i] = sublist

all_paths = np.array(all_paths)
all_paths = DataFrame(all_paths).drop_duplicates().values
realizations = list(all_paths)

n = linked_node_num
e = 3

H_list = []                                  #create an array to which desired subgraphs will be added
counter = 0
for i in range(len(realizations)):           #for all realizations (n in array nodes)...
   H = nx.subgraph(G,realizations[i])        #find subgraph (user inputs graph G and i-th realization) and call it H
   numbEdges = len(H.edges())                #compute the number of edges in subgraph H
   if numbEdges == e:                        #if H has the same number of edges as the desired (user input) e, then
      counter = counter + 1                  #counter increments (we've found a desired subgraph!)
      H_list.append(H)                       #append H to H_list
      print H.nodes()

nodes = G.nodes()
realizations = it.combinations(nodes, n)
realizations = np.array(list(realizations))

print "\n"
H_list = []                                  #create an array to which desired subgraphs will be added
counter = 0
for i in range(len(realizations)):           #for all realizations (n in array nodes)...
   H = nx.subgraph(G,realizations[i])        #find subgraph (user inputs graph G and i-th realization) and call it H
   numbEdges = len(H.edges())                #compute the number of edges in subgraph H
   if numbEdges == e:                        #if H has the same number of edges as the desired (user input) e, then
      counter = counter + 1                  #counter increments (we've found a desired subgraph!)
      H_list.append(H)                       #append H to H_list
      print H.nodes()
      print len(H.edges())





plt.show()




