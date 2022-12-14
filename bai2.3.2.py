from sympy import diff, symbols
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
g = 4*x**3 - 4 * x
k = diff(g, x)
print('dao ham bac 2 cua ham so la:', k)


def dao_ham_bac_2(a,b,x):
    f = a*x**2 - b
    return f

x = np.linspace(start = -10.0, stop = 10.0, num = 200)
y = dao_ham_bac_2(12,-4,x)

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_xlabel('Truc hoanh - x')
ax.set_ylabel('Truc tung - y')
ax.plot(x, y, label = r'$12x^{2} - 4$')
ax.set_title('do thi dao ham bac 2')

ax.legend()
plt.show()