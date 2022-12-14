import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def mat_hyperbolic(a,b,c,x,y):
    z = np.sqrt(a * (x/3)**2 + b * (y/5)**2 + c)
    return z

x = np.linspace(start = -10.0, stop = 10.0, num = 1000)
y = np.linspace(start = -10.0, stop = 10.0, num = 1000)

x,y = np.meshgrid(x,y)
z = mat_hyperbolic(4,4,-4,x,y)

fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
rosen_surf = ax.plot_surface(x, y, z, cmap=cm.gist_heat_r, linewidth=0, antialiased=False )

ax.set_zlim(-10,10)

fig.colorbar(rosen_surf, shrink=1, aspect=10)
plt.show()
