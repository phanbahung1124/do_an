
def sap_xep(x,reverse):
    if reverse == True:
        for i in range(n-1):
            for j in range(i+1,n):
                if x[i] > x[j]:
                    x[i],x[j] = x[j],x[i]
    else:
        if reverse == True:
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if x[i] < x[j]:
                        x[i], x[j] = x[j], x[i]


def main():
    reverse = str(input('True or False: '))
    sap_xep(x, reverse)

if __name__ =='__main__':
    main()