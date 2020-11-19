import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25) 
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sin(X)**2+np.cos(Y)**2
Z = +R
Z2 = -R

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
surf = ax.plot_surface(X, Y, Z2, cmap=cm.coolwarm)


# Customize the z axis.
ax.set_zlim(-np.amax(Z),np.amax(Z))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.

plt.savefig("plot3d.png",transparent = True,dpi=300)