import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools as it
import time
from sys import argv
from networkx.algorithms import isomorphism

L = 10
def distance(p1,p2,L):
  s = 0
  for i in range(len(p1)):
    dx = p1[i]-p2[i]
    s+=(dx - L*round(dx/L))**2
  return np.sqrt(s)

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
n = 4                                        #number of nodes of the desired subgraph 
e = 4                                        #number of edges of the desired subgraph

counter = 0                                  #counter to count the total number of subgraphs (n nodes, e edges) within a graph
nodes = G.nodes()                            #extract all the nodes of G

print "generating realizations ..."
######################################
realizations = it.combinations(nodes,n)      #computes all combinations of n nodes found in the nodes array. This is because...
realizations = np.array(list(realizations))  #...networkx finds subgraphs after user specifies a set of nodes within the graph...
                                             #for n=3, one realization could be (1,2,10), another is (42,89,5), etc
######################################
print "finding all subgraphs ..."
H_list = []                                  #create an array to which desired subgraphs will be added
for i in range(len(realizations)):           #for all realizations (n in array nodes)...
   H = nx.subgraph(G,realizations[i])        #find subgraph (user inputs graph G and i-th realization) and call it H
   numbEdges = len(H.edges())                #compute the number of edges in subgraph H
   if numbEdges == e:                        #if H has the same number of edges as the desired (user input) e, then
      counter = counter + 1                  #counter increments (we've found a desired subgraph!)
      H_list.append(H)                       #append H to H_list

print "checking for isomorphism ..."
orig_H_list = list(H_list)                   #make a copy of H_list and call it orig_H_list
all_types = []                               #all_types will include subgraphs partitioned by their isomorphism [[H1,H2,...],[H3,H4,...],...]
while len(H_list) > 0:                       #as long as H_list has elements in it (we will be deleting its elements soon)
   toremove = []                             #an array to store indices of elements to be removed
   types = []                                #temporary array of isomorphs (or "types") to be appended to all_types soon
   for i in range(len(H_list)):              #for all elements in H_list
       GM = isomorphism.GraphMatcher(H_list[0], H_list[i])           #check for isomorphism between first element and all other elements in H_list using networkx
       if (GM.is_isomorphic()==True):                                #if two graphs are isomorphs
           toremove.append(i)                                        #add its index to toremove
           types.append(H_list[i])                                   #append it to types
   H_list = [i for j, i in enumerate(H_list) if j not in toremove]   #remove elements of H_list corresponding to indicies in toremove         
   all_types.append(types)                                           #append types to all_types

print "plotting ..."
for i in range(len(all_types)):                                      #for all isomorphs
   plt.figure(i,figsize=(10,10))  
   plt.title("There are %d subgraphs with %d nodes and %d edges\n This subgraph has %d isomorph(s)\n\n This is isomorph %d of %d"%(counter,n,e,len(all_types),i+1,len(all_types)))
   nx.draw(G,mypos,alpha=0.6)                                                   #draw the entire graph G with transparency alpha
   nx.draw_networkx_labels(G,mypos)                                             #draw the entire graph G at positions stored in mypos and label each node
   nx.draw_networkx_edges(all_types[i][0],mypos,width=3.0,edge_color='blue')    #draw the first subgraph in i-th isomorph list with blue outlines

edges = G.edges()
distances = {}
for i in range(len(edges)):
    j = edges[i][0]
    k = edges[i][1]
    d = distance((x_pos[j],y_pos[j]),(x_pos[k],y_pos[k]),L)
    distances[(j,k)] = d


############################################
end = time.clock()
print "TIME (in sec): ", (end - start)
print "For %d nodes and %d edges, there are ..."%(n,e)
print "NUMBER OF SUBGRAPHS: ", counter
print "NUMBER OF ISOMORPHS (TYPES): ", len(all_types)                            
print "DISTANCES BETWEEN NODES: ", distances
plt.show()
