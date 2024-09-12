# write a program to find greatest of three Numbers


def greatest (a, b, c):

    if(a>b and a>c):
        return a

    elif(b>a and b>c):
        return b

    else:
        (c>a and c>b)
        return c


a=10
b=20
c=45
print("The greatest number is: ",greatest(a,b,c))

