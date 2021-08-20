#finding target
class Leet1:
    def __init__(self,target,ary):
        self.target=target
        self.arrf=ary
    def findingind(self):
        arr=self.target
        arrf=self.arrf
        check=1
        for i in range(len(arrf)):
            print(arrf[i]+arrf[check])
            if arrf[i]+arrf[check]==arr:
                print(arrf[i],arrf[check])
                break
        #print(arrf.index(i))
arrf=[1,3,2]
le=Leet1(3,arrf)
le.findingind()