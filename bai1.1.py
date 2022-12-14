import numpy as np


def sinh_ngau_nhien(a,b,n):
    x = (b-a)*np.random.random()+a
    for i in range(n):
        print(x)

def main():
    a = float(input('nhap so thuc a: '))
    b = float(input('nhap vao so thuc b: '))
    n = int(input('nhap vao so nguyen n:'))
    sinh_ngau_nhien(a,b,n)


if __name__ =='__main__':
    main()