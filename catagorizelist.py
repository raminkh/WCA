import numpy as np
import matplotlib.pyplot as plt

mylist = ['A','A','B','A','D','A','A','B','C','B']
orig_list = list(mylist)
all_types = []
while len(mylist) > 0:
   toremove = []
   types = []
   for i in range(len(mylist)):
       cond = mylist[0] == mylist[i]
       if cond==True:
           toremove.append(i)
           types.append(mylist[i])
   mylist = [i for j, i in enumerate(mylist) if j not in toremove]         
   all_types.append(types)
print all_types



     

