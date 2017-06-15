import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools as it
import time
from sys import argv
from networkx.algorithms import isomorphism
from pandas import *

def distance(p1,p2,L):
  s = 0
  for i in range(len(p1)):
    dx = p1[i]-p2[i]
    s+=(dx - L*round(dx/L))**2
  return np.sqrt(s)

def dfs_paths(graph, start, goal, linked_node):
   stack = [(start, [start])]
   while stack:
      (vertex, path) = stack.pop()
      for k in set(graph[vertex]) - set(path):
         if k == goal or len(path) == linked_node:
            yield path + [k]
         else:
            stack.append((k, path + [k]))

def generate_realizations_combinatorics(G, n):
   nodes = G.nodes()
   realizations = it.combinations(nodes,n) 
   realizations = np.array(list(realizations)) 
   return realizations

def find_subgraphs(G,realizations,n,e):
   H_list = []                               
   counter = 0
   for i in range(len(realizations)):        
      if len(realizations[i]) != n:
         print "WARNING: realization (%d)'s length is not n."%i
      H = nx.subgraph(G,realizations[i])     
      numbEdges = len(H.edges())             
      if numbEdges == e:                     
         counter = counter + 1               
         H_list.append(H)      
   return (H_list, counter)

def generate_adjList(G):
   adjList = {}
   nodes = len(G.nodes())
   for i in range(nodes):
      adjList[i] = G.neighbors(i)
   return adjList

def generate_realizations(adjList, linked_node_num):
   all_paths = []
   nodes = len(adjList)
   for i in range(len(adjList)):
      for j in range(len(adjList)):
         paths = list(dfs_paths(adjList, i, j, linked_node_num))
         index = []
         for k in range(len(paths)):
            if len(paths[k]) < linked_node_num:
               index.append(k)
            else:
               paths[k] = paths[k][:linked_node_num]
         paths = [l for m, l in enumerate(paths) if m not in index]
         all_paths.append(paths)
   
   all_paths = sum(all_paths,[])
   [k.sort() for k in all_paths]
   all_paths = np.array(all_paths)
   all_paths = DataFrame(all_paths).drop_duplicates().values
   realizations = list(all_paths)
   return realizations

def check_isomorphism(H_list):
   orig_H_list = list(H_list)                 
   all_types = []                             
   while len(H_list) > 0:                     
      toremove = []                           
      types = []                              
      for i in range(len(H_list)):            
          GM = isomorphism.GraphMatcher(H_list[0], H_list[i])         
          if (GM.is_isomorphic()==True):                              
              toremove.append(i)                                      
              types.append(H_list[i])                                 
      H_list = [i for j, i in enumerate(H_list) if j not in toremove] 
      all_types.append(types)     
   return all_types

def generate_distances(G):
   edges = G.edges()
   distances = {}
   for i in range(len(edges)):
       j = edges[i][0]
       k = edges[i][1]
       d = distance((x_pos[j],y_pos[j]),(x_pos[k],y_pos[k]),L)
       distances[(j,k)] = d
   return distances

start = time.clock()                         #start measuring time
positions = np.loadtxt('traj.xyz')           #load positions from simulation output file (this is used for plotting the graph)
x_pos = positions[:,2]                       #store x positions in x_pos
y_pos = positions[:,3]                       #store y positions in y_pos
mypos = {}                                
for i in range(len(x_pos)):
   mypos[i] = [x_pos[i], y_pos[i]]           #fill in mypos (a dictionary) with x and y positions, later to be sent to networkx's plotting command

M = np.loadtxt('adjMatrix.out')              #load adjacency matrix and call it M
np.fill_diagonal(M,0)                        #make sure diagonal elements are zero
if (not (M.transpose() == M).all()):         #make sure M is symmetric (prints True if so)
   print "WARNING: adjacency matrix is not symmetric."
G = nx.from_numpy_matrix(M)                  #create a networkx graph G from adjacency matrix M

############################################
L = 10
linked_node_num = 3 
n = linked_node_num                          #number of nodes of the desired subgraph 
e = 2                                        #number of edges of the desired subgraph

adjList = generate_adjList(G)

print "generating realizations ..."
realizations = generate_realizations(adjList,linked_node_num)

print "finding all subgraphs ..."
(H_list, counter) = find_subgraphs(G, realizations, n, e)

print "checking for isomorphism ..."
all_types =  check_isomorphism(H_list)

print "plotting ..."
for i in range(len(all_types)):                                      #for all isomorphs
   plt.figure(i,figsize=(10,10))  
   plt.title("There are %d subgraphs with %d nodes and %d edges\n This subgraph has %d isomorph(s)\n\n This is isomorph %d of %d"%(counter,n,e,len(all_types),i+1,len(all_types)))
   nx.draw(G,mypos,alpha=0.6)                                                   #draw the entire graph G with transparency alpha
   nx.draw_networkx_labels(G,mypos)                                             #draw the entire graph G at positions stored in mypos and label each node
   nx.draw_networkx_edges(all_types[i][0],mypos,width=3.0,edge_color='blue')    #draw the first subgraph in i-th isomorph list with blue outlines

distances = generate_distances(G)

############################################
end = time.clock()
print "TIME (in sec): ", (end - start)
print "For %d nodes and %d edges, there are ..."%(n,e)
print "NUMBER OF SUBGRAPHS: ", counter
print "NUMBER OF ISOMORPHS (TYPES): ", len(all_types)                            
print "DISTANCES BETWEEN NODES: ", distances
plt.show()
