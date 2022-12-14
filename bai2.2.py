from sympy import *

def giai_he_phuong_trinh(x,y,z):
    eq1 = Eq(x * 2 - 5 * y + z, -5)
    eq2 = Eq(4 * x + 2 * y - 2 * z, 2)
    eq3 = Eq(x + y - z, 0)
    a = solve((eq1, eq2, eq3), (x, y, z))
    print('he phuong trinh co nghiem la: ',a)

def tinh_gioi_han(x):
    f = ((x**3 - 3*x**2)**(1/3) + sqrt(x**2 - 2*x))
    b = limit(f,x,oo)
    print('gioi han cua phuong trinh la:',b)

def tinh_dao_ham(x):
    k = (2*x -1) / (x + 2)
    c = diff(k,x)
    print('dao ham cua phuon trinh la:',c)

def tinh_nguyen_ham(x):
    l = x / (x**2 + 1)
    d = integrate(l,x)
    print('nguyen ham cua ham so la: ',d)

def tinh_tich_phan(x):
    j = ((1 - x * tan(x)) / (x**2 * cos(x) + x))
    e = integrate(j, (x, (2*pi)/3, pi))
    print('tich phan cua ham so la: ',e)

def main():
    x,y,z = symbols('x y z')
    giai_he_phuong_trinh(x,y,z)
    tinh_gioi_han(y)
    tinh_dao_ham(x)
    tinh_nguyen_ham(x)
    tinh_tich_phan(x)

if __name__ =='__main__':
    main()

