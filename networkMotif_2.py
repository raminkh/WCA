import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools as it
import time
from sys import argv
from networkx.algorithms import isomorphism

start = time.clock()
positions = np.loadtxt('traj.xyz')
x_pos = positions[:,2]
y_pos = positions[:,3]
mypos = {}
for i in range(len(x_pos)):
   mypos[i] = [x_pos[i], y_pos[i]]

M = np.loadtxt('adjMatrix.out')
np.fill_diagonal(M,0)
print (M.transpose() == M).all()
G = nx.from_numpy_matrix(M)

nx.draw(G,mypos,alpha=0.6)
nx.draw_networkx_labels(G,mypos)

n = 4
e = 6

plot_counter = 0#int(argv[1])
counter = 0
nodes = G.nodes()
print "generating realizations ..."
realizations = it.combinations(nodes,n)
realizations = np.array(list(realizations))
print "finding all subgraphs ..."
H_list = []
for i in range(len(realizations)):
   H = nx.subgraph(G,realizations[i])
   numbEdges = len(H.edges())
   if numbEdges == e:
      counter = counter + 1
      H_list.append(H)
      if counter == plot_counter:
         nx.draw_networkx_edges(H,mypos,width=3.0,edge_color='blue')
print "checking for isomorphism ..."

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
print "NUMBER OF TYPES: ", len(all_types)

##################################      
end = time.clock()
print "TIME: ", (end - start)
print "NUMBER OF SUBGRAPHS: ", counter
