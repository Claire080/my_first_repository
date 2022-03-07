class Sycarus:
    
    def __init__(self,m):
        self.n=m #liste contenant la suite de sycarus.

    def get(self):
        return self.n

    def set(self,m=14):
        self.n=m
        return self.n

    def write_sycarus_in_file(self):
        S=[self.n]
        while(S.count(1)!=4):
            if(self.n%2==0):
                self.n=self.n/2
                S.append(int(self.n))
            elif(self.n%2!=0):
                self.n=(self.n*3)+1
                S.append(int (self.n))
                
        f=open("f_sycarus.txt","w")
        f.write(str(S))
        f.close()

    def read_in_file(self):
        f=open("f_sycarus.txt","r")
        print(f.read())
        f.close()
    
        
        
