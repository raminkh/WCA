import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools as it
import time
from sys import argv
from networkx.algorithms import isomorphism

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

#RUNS DOWN NODES UNTIL ALL NODES ARE VISITED (A UNIQUE PATH IS GIVEN)
#print list(nx.dfs_edges(G,2))
print list(nx.edge_dfs(G,0))

plt.show()
