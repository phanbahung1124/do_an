import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def mat_cau(x,y,z):
    k = (x+2)**2 + (y-1)**2 + (z-4)**2
    return k

x = np.linspace(start = -10.0, stop = 10.0, num = 1000)
y = np.linspace(start = -10.0, stop = 10.0, num = 1000)
z = np.linspace(start = -10.0, stop = 10.0, num = 1000)

x,y = np.meshgrid(x,y)
k = mat_cau(x,y,z)

fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
rosen_surf = ax.plot_surface(x, y, k, cmap=cm.gist_heat_r, linewidth=0, antialiased=False )

ax.set_zlim(-10,10)

fig.colorbar(rosen_surf, shrink=1, aspect=10)
plt.show()
