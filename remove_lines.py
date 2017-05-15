import numpy as np
import matplotlib.pyplot as plt

N = 196
f = open("traj.xyz","r")
lines = f.readlines()
f.close()
length = len(lines)
delArray = []
chunk = np.arange(0,9)
delArray.append(chunk)
end = chunk[8]
while (end+N+2)<length:
   start = chunk[8] + (N+1)
   end = chunk[8] + (N+1) + 8
   chunk = np.arange(start,end+1)
   delArray.append(chunk)
delArray = np.array(delArray)
delArray.flatten()
goodLines = []
for line in range(length):
   if line not in delArray:
      goodLines.append(line)
f2 = open("traj.xyz","w")
for i in goodLines:
   f2.write(lines[i])
f2.close()

