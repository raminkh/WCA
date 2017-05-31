#Ramin Khajeh
#05/19/17
#Counts the number of a particular subgraph specified by the number of nodes and edges 

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools as it
import time 

start = time.clock()
positions = np.loadtxt('traj.xyz')
x_pos = positions[:,2]
y_pos = positions[:,3]
mypos = {}
G = nx.Graph()
for i in range(len(x_pos)):
    mypos[i] = [x_pos[i], y_pos[i]]
    G.add_node(i)

nx.draw(G,mypos)
nx.draw_networkx_labels(G,mypos)
plt.show()

M = np.loadtxt('adjMatrix.out')
np.fill_diagonal(M, 0)
print (M.transpose() == M).all()
G = nx.from_numpy_matrix(M)


def draw(G):#have pos as an input to this func
   #pos = nx.circular_layout(G)
   pos = mypos
   print pos
   nx.draw(G,pos)
   nx.draw_networkx_labels(G,pos)
   plt.show()

#counts the number of subgraphs specified by number of nodes n and number of edges e
#for instance, a wedge corresponds to n = 3, e = 2
def subgraph(G,n,e):
   plot_counter = 0
   counter = 0
   nodes = G.nodes()
   realizations = it.combinations(nodes,n)
   realizations = np.array(list(realizations))  
   for i in range(len(realizations)):
      H = nx.subgraph(G,realizations[i])
      #including the following (commented) line will draw each subgraph 
      #draw(H)
      numbEdges = len(H.edges())
      if numbEdges == e:
         counter = counter + 1
         if plot_counter < 6: 
            draw(H)
            plot_counter=plot_counter + 1;
   return counter

#generates a random symmetrix sparse matrix of ones and zeros (with zeros having a higher 
#probability) that resembles the adjacency matrix we obtain from LJ liquid simulations.  
M = np.loadtxt('adjMatrix.out')
#N = 10
#M = np.random.choice([0,1],p=[0.80,0.20],size=(N,N))
#M = np.tril(M) + np.tril(M,-1).T
np.fill_diagonal(M, 0)
print (M.transpose() == M).all()
G = nx.from_numpy_matrix(M)

#a simple test case that's commented out
#G = nx.Graph()
#G.add_node(1)
#G.add_node(2)
#G.add_node(3)
#G.add_node(4)
#G.add_node(5)
#G.add_edge(1,2)
#G.add_edge(2,3)
#G.add_edge(4,5)
#G.add_edge(2,5)
#G.add_edge(5,1)
#draw(G)

#consider a wedge
n_tri = 3
e_tri = 2

#n_tet = 3
#e_tet = 3
print "number of subgraphs with %.0f nodes and %.0f edges is..."%(n_tri,e_tri), subgraph(G,n_tri,e_tri)
#print "number of subgraphs with %.0f nodes and %.0f edges is..."%(n_tet,e_tet), subgraph(G,n_tet,e_tet)



end = time.clock()
print "time...", (end - start)
