import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('wca.rdf')
plt.plot(data[:,1],data[:,2],'o')
plt.xlabel('r')
plt.ylabel('g(r)')
plt.show()
