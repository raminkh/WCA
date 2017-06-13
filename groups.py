#copied for safety on 01/02/2016
import numpy as np
import matplotlib.pyplot as plt

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

#2D C-Shape
#graph = {0: [1,2,3,4,5], 1: [0,2], 2: [0,1,3], 3: [0,2,4], 4: [0,3,5], 5: [0,4]}

#2D U-Shape
graph = {0: [1,2], 1: [0,2,3], 2: [0,1,3,4], 3: [1,2,4,5], 4: [2,3,5], 5: [3,4]}
rot = {0:5, 1:4, 2:3, 3:2, 4:1, 5:0} 

#Polytetrahedron Graph      
#graph = {0: [1,4,5], 1: [0,2,3,4,5], 2: [1,3,4], 3: [1,2,4,5], 4: [0,1,2,3,5], 5: [0,1,3,4]}
#rot = {0:2, 1:4, 2:0, 3:5, 4:1, 5:3}
 
#Octahedron Graph
graph = {0: [1,2,3,4], 1: [0,2,4,5], 2: [0,1,3,5], 3: [0,2,4,5], 4: [0,1,3,5], 5: [1,2,3,4]}
rot_P17_1 = {0:2, 1:0, 2:1, 3:5, 4:3, 5:4}
rot_P17_2 = {0:1, 1:2, 2:0, 3:4, 4:5, 5:3}
rot_P35_1 = {0:3, 1:2, 2:5, 3:4, 4:0, 5:1}
rot_P35_2 = {0:4, 1:5, 2:1, 3:0, 4:3, 5:2}
rot_P46_1 = {0:4, 1:0, 2:3, 3:5, 4:1, 5:2}
rot_P46_2 = {0:1, 1:4, 2:5, 3:2, 4:0, 5:3}
rot_P28_1 = {0:2, 1:5, 2:3, 3:0, 4:1, 5:4}
rot_P28_2 = {0:3, 1:4, 2:0, 3:2, 4:5, 5:1}
rot_Eac = {0:2, 1:3, 2:0, 3:1, 4:5, 5:4}
rot_Eab = {0:1, 1:0, 2:4, 3:5, 4:2, 5:3}
rot_Ebc = {0:5, 1:2, 2:1, 3:4, 4:3, 5:0}
rot_Ebe = {0:5, 1:4, 2:3, 3:2, 4:1, 5:0}
rot_Ebf = {0:3, 1:5, 2:4, 3:0, 4:2, 5:1}
rot_Eae = {0:4, 1:3, 2:5, 3:1, 4:0, 5:2}
rot_Vbd_1 = {0:2, 1:1, 2:5, 3:3, 4:0, 5:4}
rot_Vce_1 = {0:1, 1:5, 2:2, 3:0, 4:4, 5:3}
rot_Vce_2 = {0:3, 1:0, 2:2, 3:5, 4:4, 5:1}
rot_Vbd_2 = {0:4, 1:1, 2:0, 3:3, 4:5, 5:2}
rot_Vce_3 = {0:5, 1:3, 2:2, 3:1, 4:4, 5:0}
rot_Vbd_3 = {0:5, 1:1, 2:4, 3:3, 4:2, 5:0}
rot_Vaf_1 = {0:0, 1:2, 2:3, 3:4, 4:1, 5:5}
rot_Vaf_2 = {0:0, 1:4, 2:1, 3:2, 4:3, 5:5}
rot_Vaf_3 = {0:0, 1:3, 2:4, 3:1, 4:2, 5:5}

#def dfs_iter(graph,root):
#   visited = []
#   stack = [root,]
#   while stack:
#      node = stack.pop()
#      if node not in visited:
#         visited.append(node)
#         stack.extend([x for x in graph[node] if x not in visited])
#
#   return visited

#Outputs list of all the possible paths of going from root to target
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

#x =  list(dfs_paths(graph,0,5))

#removing paths that don't hit all vertices
states = []
for k in range(len(x)):
   for i in range(len(x[k])):
      if len(x[k][i]) == N:
         states.append(x[k][i])
print "states are : ","\n", states
print np.shape(states)

#Checking for repetitions (unnecessary because of i+1 in for loop)
index = []
for i in np.arange(np.shape(states)[0]):
   for j in np.arange(i+1,np.shape(states)[0]):
      test = compare(states[i],states[j])
      if test == True:
         index.append([i,j])
print index

rot_states = list(states)
degeneracies = 0
for i in np.arange(len(states)):
   rot_states[i] = [rot[j] for j in rot_states[i]]
   degen_test_1 = compare(rot_states[i],states[i])
   degen_test_2 = compare(rot_states[i][::-1],states[i])
   if (degen_test_1 == True or degen_test_2 == True):
      degeneracies = degeneracies + 1
#NOTEEE THAT DIVIDING BY TWO WORKS FOR 180 DEGREE ROTATIONS
state_number = (len(states) - degeneracies)/2.0 + (degeneracies/2.0)
print "degeneracies number is ", degeneracies
print "state_number is : ", state_number
print "\n"
print states
print "\n"
print rot_states

