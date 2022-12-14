from sympy import diff, symbols
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
g = 12*x**2 - 4
k = diff(g, x)
print('dao ham bac 3 cua ham so la:', k)


def dao_ham_bac_3(a,x):
    f = a*x
    return f

x = np.linspace(start = -10.0, stop = 10.0, num = 200)
y = dao_ham_bac_3(12,x)

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_xlabel('Truc hoanh - x')
ax.set_ylabel('Truc tung - y')
ax.plot(x, y, label = r'$24x$')
ax.set_title('do thi dao ham bac 3')

ax.legend()
plt.show()