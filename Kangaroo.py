def kangaroo(x1,v1,x2,v2):
    for k in range(10001):
            if ((x1+v1)==(x2+v2)):
            return 'YES'
        x1+=v1
        x2+=v2
    return 'NO'