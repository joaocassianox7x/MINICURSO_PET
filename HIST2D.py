"""
HISTOGRAMA EM DUAS DIMENSÕES.
"""

import numpy as np
import matplotlib.pyplot as plt


dim = 10000
mean = [0,0]
cov = [[1,0],[0,1]]

x,y = np.random.multivariate_normal(mean,cov,dim).T

plt.hist2d(x,y,bins=int(np.sqrt(dim)))
plt.xlabel("x")
plt.ylabel("y")

plt.colorbar() #documentacao em https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.colorbar.html

plt.tight_layout()
plt.savefig("hist2d.png",dpi = 300)

