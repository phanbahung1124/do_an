import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def yen_ngua(x,y):
    z = (x / 3)**2 - (y/2)**2
    return z

x = np.linspace(start = -2.5, stop = 2.0, num = 1000)
y = np.linspace(start = -2.0, stop = 2.5, num = 1000)

x,y = np.meshgrid(x,y)
z = yen_ngua(x, y)

fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
rosen_surf = ax.plot_surface(x, y, z, cmap=cm.gist_heat_r, linewidth=0, antialiased=False )

ax.set_zlim(-2, 2)

fig.colorbar(rosen_surf, shrink=0.5, aspect=5)
plt.show()

