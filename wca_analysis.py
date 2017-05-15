import numpy as np
import matplotlib.pyplot as plt
from sys import argv

def distance(p1,p2,L):
  s = 0
  for i in range(len(p1)):
    dx = p1[i]-p2[i]
    s+=(dx - L*round(dx/L))**2
  return np.sqrt(s)

data = np.loadtxt('traj.xyz')
d_cut = 0.5
x = data[:,2]
y = data[:,3]
N = len(x)
boxL = int(argv[1])
adjMatrix = np.zeros([N,N])
for i in range(N):
    for j in range(N):
        d = distance((x[i],y[i]),(x[j],y[j]),boxL)
        if d<d_cut:
            adjMatrix[i,j] = 1
        else:
            adjMatrix[i,j] = 0
print adjMatrix
