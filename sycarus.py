#conjecture de sycarus

def sycarus(n):
    L=[n]
    while(L.count(1)!=4):
        if(n%2==0):
            n=n/2
            L.append(int(n))
        elif(n%2!=0):
            n=(n*3)+1
            L.append(int (n))
    return L
