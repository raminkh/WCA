#Ramin Khajeh
#01/03/2016
#Calculates the rotational entropy of a given structure
import numpy as np
import matplotlib.pyplot as plt
import argparse

def compare(a,b):#a and b have to have length of N
   N = 6
   agreement = []
   for i in np.arange(len(a)):
      if a[i] == b[i]:
         agreement.append(True)
      else:
         agreement.append(False)
   if np.sum(agreement)==N:
      return True
   else:
      return False


############### CIRCULAR-SHAPE IN 2D ##########################
#graph = {0: [1,2,3,4,5], 1: [0,2], 2: [0,1,3], 3: [0,2,4], 4: [0,3,5], 5: [0,4]}

############### STACHED-SHAPE IN 2D ##########################
#graph = {0: [1,2], 1: [0,2,3], 2: [0,1,3,4], 3: [1,2,4,5], 4: [2,3,5], 5: [3,4]}
#rot = [{0:5, 1:4, 2:3, 3:2, 4:1, 5:0}]

############### POLYTETRAHEDRON ################################
#graph = {0: [1,4,5], 1: [0,2,3,4,5], 2: [1,3,4], 3: [1,2,4,5], 4: [0,1,2,3,5], 5: [0,1,3,4]}
#rot = [{0:2, 1:4, 2:0, 3:5, 4:1, 5:3}]
 
############### OCTAHEDRON ################################
graph = {0: [1,2,3,4], 1: [0,2,4,5], 2: [0,1,3,5], 3: [0,2,4,5], 4: [0,1,3,5], 5: [1,2,3,4]}

P17_1 = {0:2, 1:0, 2:1, 3:5, 4:3, 5:4}
P17_2 = {0:1, 1:2, 2:0, 3:4, 4:5, 5:3}
P35_1 = {0:3, 1:2, 2:5, 3:4, 4:0, 5:1}
P35_2 = {0:4, 1:5, 2:1, 3:0, 4:3, 5:2}
P46_1 = {0:4, 1:0, 2:3, 3:5, 4:1, 5:2}
P46_2 = {0:1, 1:4, 2:5, 3:2, 4:0, 5:3}
P28_1 = {0:2, 1:5, 2:3, 3:0, 4:1, 5:4}
P28_2 = {0:3, 1:4, 2:0, 3:2, 4:5, 5:1}
Eac = {0:2, 1:3, 2:0, 3:1, 4:5, 5:4}
Eab = {0:1, 1:0, 2:4, 3:5, 4:2, 5:3}
Ebc = {0:5, 1:2, 2:1, 3:4, 4:3, 5:0}
Ebe = {0:5, 1:4, 2:3, 3:2, 4:1, 5:0}
Ebf = {0:3, 1:5, 2:4, 3:0, 4:2, 5:1}
Eae = {0:4, 1:3, 2:5, 3:1, 4:0, 5:2}
Vbd_1 = {0:2, 1:1, 2:5, 3:3, 4:0, 5:4}
Vce_1 = {0:1, 1:5, 2:2, 3:0, 4:4, 5:3}
Vce_2 = {0:3, 1:0, 2:2, 3:5, 4:4, 5:1}
Vbd_2 = {0:4, 1:1, 2:0, 3:3, 4:5, 5:2}
Vce_3 = {0:5, 1:3, 2:2, 3:1, 4:4, 5:0}
Vbd_3 = {0:5, 1:1, 2:4, 3:3, 4:2, 5:0}
Vaf_1 = {0:0, 1:2, 2:3, 3:4, 4:1, 5:5}
Vaf_2 = {0:0, 1:4, 2:1, 3:2, 4:3, 5:5}
Vaf_3 = {0:0, 1:3, 2:4, 3:1, 4:2, 5:5}

rot = [P17_1, P17_2, P35_1, P35_2, P46_1, P46_2, P28_1, P28_2, Eac, Eab, Ebc, Ebe, Ebf, Eae, Vbd_1, Vce_1, Vce_2, Vbd_2, Vce_3, Vbd_3, Vaf_1, Vaf_2, Vaf_3]


# Outputs list of all the possible paths of going from root to target
def dfs_paths(graph, root, target, path=None):
   if path is None:
      path = [root]

   if root == target:
      yield path

   for vertex in [x for x in graph[root] if x not in path]:
      for each_path in dfs_paths(graph,vertex,target,path+[vertex]):
         yield each_path

x=[]
N = 6
for i in np.arange(N):
   for j in np.arange(i+1,N):
      x.append(list(dfs_paths(graph,i,j)))

# Removing paths that don't hit all vertices
states = []
for k in range(len(x)):
   for i in range(len(x[k])):
      if len(x[k][i]) == N:
         states.append(x[k][i])
print "initial size of states is : ", np.shape(states)

# Checking for repetitions (unnecessary because of i+1 in the for loop above)
index = []
for i in np.arange(np.shape(states)[0]):
   for j in np.arange(i+1,np.shape(states)[0]):
      test = compare(states[i],states[j])
      if test == True:
         index.append([i,j])
#print index
#########################################################################################
def rotate_state(s):
   rot_s = []
   for k in np.arange(len(rot)):
      r = rot[k]
      rot_s.append([r[j] for j in s])
   return rot_s

## Removing structures that are repeated upon rotation
indices = []
for i in np.arange(len(states)):
   rot_states = rotate_state(states[i])
   for j in np.arange(i+1,len(states)):
      for k in range(len(rot_states)):
         my_comparison_1 = compare(states[j],rot_states[k])
         my_comparison_2 = compare(states[j],rot_states[k][::-1])
         if (my_comparison_1==True or my_comparison_2==True):
            indices.append(j)
new_states = [i for j, i in enumerate(states) if j not in indices]
print "distinct structures are : ", new_states

################################ DISTINCT STATES HAVE BEEN CREATED NOW ################
# calculating degeneracies of each structure 
rot_states = list(new_states)
degeneracies = 0
for i in np.arange(len(new_states)):
   rot_states = rotate_state(new_states[i])
   for k in range(len(rot_states)):
      my_comp_1 = compare(new_states[i],rot_states[k])
      my_comp_2 = compare(new_states[i],rot_states[k][::-1])
      if (my_comp_1 == True or my_comp_2 == True):
          degeneracies = degeneracies + 1 

# Note: dividing by 2.0 only works if symmetries are DOUBLY degenerate
yield_number = (len(new_states) - degeneracies) + (degeneracies / 2.0)
print "\n"
print "size of states is now: ", len(new_states)
print "degeneracies are: ", degeneracies
print "yield number is : ", yield_number

