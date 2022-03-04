#multiplication égyptienne

def puissance2(x):
    i=1
    y=0
    while(y<=x):
        y=2**i
        i+=1
    return y//2 #fonction qui retourne la plus grande puissance de x <=x

def mul(a,b):
    i=1
    x=max(a,b)
    y=min(a,b)

    if(y==1):
        return x
    elif(y==0):
        return y
    else:
        d={i:x}
        mult=0
        while True:
            x+=x
            i+=i
            if(i>y):
                break
            d[i]=x

        while(y!=0):
            mult+=d[puissance2(y)]
            y=y-puissance2(y)
            
        return mult
