import numpy as np
#1.1
def ham_tich(A,m,n,x):
    a = x * A
    print('nhan ma tran voi mot vo huong:', a)

#1.2
def nhan_hadamard(A,B,m,n):
    b = np.multiply(A, B)
    print('nhan hadamard:', b)
#1.2
def nhan_chuyen_vi(A,B):
    c = np.inner(A, B)
    print('nhan ma tran voi ma tran chuyen vi:', c)

#1.3
def main():
    m = abs(int(input('nhap vao so nguyen m: ')))
    n = abs(int(input('nhap vao so nguyen n: ')))
    x = abs(float(input('nhap vao so thuc x: ')))
    A = np.random.rand(m,n)
    B = np.random.rand(m,n)
    ham_tich(A,m,n,x)
    nhan_hadamard(A,B,m,n)
    nhan_chuyen_vi(A,B)


if __name__ =='__main__':
    main()
