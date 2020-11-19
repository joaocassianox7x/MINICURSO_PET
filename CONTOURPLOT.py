"""
CONTOURPLOT, UM TIPO DE HISTOGRAMA EM ALTA DEFINIÇÃO!
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
x = np.arange(0,10,0.05)
y = np.arange(0,10,0.05)

x,y = np.meshgrid(x,y)
z = np.sin(x)**2+np.cos(y)**2


fig = plt.figure()
cb = plt.contour(x,y,z,levels=15,cmap=cm.inferno)
plt.title("Levels = 15")
plt.tight_layout()
plt.savefig("contour15.png",transparent = True,dpi=300)

