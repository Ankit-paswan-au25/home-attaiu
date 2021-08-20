class Mtrx:
    def __init__(self,mat):
        self.matrix=mat
    def antidigonal(self):
        print("Answer no 1")
        matrix=self.matrix
        a=0
        b=-1
        for i in range(int(len(matrix[0]))):
            print(matrix[a][b])
            a+=1
            b+=-1 
    def sumbdrelmt(self,):
        print("Answer no 2")
        a=self.matrix
        row=len(a[0])
        col=len(a)
        sum=0
        sum1=0
        sum2=0
        sum3=0
        for i in range(row):
            for j in range(col):
                if i==0:
                    #print(a[i][j])
                    sum=sum+a[i][j]
                elif i==row-1:
                    sum1=sum1+a[i][j]
                    #print(a[i][j])
                elif j==0:
                    sum2=sum2+a[i][j]
                    #print(a[i][j])
                elif j==col-1:
                    sum3=sum3+a[i][j]
                    #print(a[i][j])

        total=sum+sum1+sum2+sum3
        print("Addition of total border elemnts is Total= ",total)
    def returnsumofrows(self):
        print("Answer no 3")
        a=self.matrix
        row=len(a[0])
        col=len(a)
        lst=[]
        sum=0
        for i in range(row):
            for j in range(col):
                sum=sum+a[i][j]
            lst.append(sum)
            sum=0
        print(lst)




mat=[]
usrip=int(input("enter row numbers"))
uerip1=int(input("enter column number"))
for i in range(usrip):
    temparr=[]
    for j in range(uerip1):
        t=int(input("enter valu row wise"))
        temparr.append(t)
    mat.append(temparr) 
mt=Mtrx(mat)
mt.antidigonal()
mt.sumbdrelmt()
mt.returnsumofrows()