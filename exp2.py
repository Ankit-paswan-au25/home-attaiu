# taking int,convertint into string returning in string
class exp2: 
    def __init__(self,arr):
        self.arrusr=arr
    def inttostrg(self):
        a=self.arrusr
        b=[str(i) for i in a]
        c="".join(b)
        d=int(c)+1
        e=str(d)
        f=[]
        for i in e:
	        if i==0:
		        g=a.pop()
		        h=g+1
		        a.append(h)
	        f.append(int(i))
	
        print(f) 
l=[]
n=int(input("enter value for array"))
for k in range(n):
    m=int(input("enter element of array"))
    l.append(m)
exper=exp2(l)
exper.inttostrg()