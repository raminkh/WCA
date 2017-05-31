import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools as it
import time
from sys import argv

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

n = 3
e = 3

plot_counter = int(argv[1])
counter = 0
nodes = G.nodes()
realizations = it.combinations(nodes,n)
realizations = np.array(list(realizations))
for i in range(len(realizations)):
   H = nx.subgraph(G,realizations[i])
   numbEdges = len(H.edges())
   if numbEdges == e:
      counter = counter + 1
      if counter == plot_counter:
         nx.draw_networkx_edges(H,mypos,width=3.0,edge_color='blue')




end = time.clock()
print "time...", (end - start)
print counter
plt.show()
