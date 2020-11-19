import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



n_pts = 64
x = np.linspace(-10,10,n_pts)
y = np.linspace(-10,10,n_pts)

x,y = np.meshgrid(x,y)

ex = x/np.linalg.norm(x**2+y**2)**2
ey = y/np.linalg.norm(x**2+y**2)**2

mod = (ex**2+ey**2)/np.linalg.norm(ex**2+ey**2)

plt.subplot(211)
VEC_PLOT = plt.quiver(x,y,ex,ey,mod)
plt.xlim(np.amin(x),np.amax(x))
plt.ylim(np.amin(y),np.amax(y))
plt.colorbar()
plt.tight_layout()


plt.subplot(212)
z = 1/np.sqrt((x**2+y**2))**3
contour_plot = plt.contour(x,y,z,levels = 600,cmap = cm.inferno)
plt.xlim(np.amin(x),np.amax(x))
plt.ylim(np.amin(y),np.amax(y))
plt.colorbar()

plt.tight_layout()
plt.savefig("exercicio.png",transparent = False,dpi=300)