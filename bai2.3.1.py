from sympy import diff, symbols
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
o = x ** 4 - 2 * x ** 2 - 3
k = diff(o, x)
print('dao ham bac 1 cua ham so la:', k)


def dao_ham_bac_1(a,b,x):
    f = a*x**3 - b*x
    return f

x = np.linspace(start = -10.0, stop = 10.0, num = 200)
y = dao_ham_bac_1(4,-4,x)

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_xlabel('Truc hoanh - x')
ax.set_ylabel('Truc tung - y')
ax.plot(x, y, label = r'$4x^{3} - 4x$')
ax.set_title('do thi dao ham bac 1')

ax.legend()
plt.show()
