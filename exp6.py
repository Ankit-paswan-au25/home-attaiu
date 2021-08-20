class Matrx:
    def __init__(self,):
        self.mati=[
            [0,1,2],
            [0,1,2],
            [0,1,2]
        ]
    def prntantidia(self):
        antidia=self.mati
        print(self.mati[0][2])
        print(self.mati[1][1])
        print(self.mati[2][0])
    def sumofbrdrelmnt(self):
        a=self.mati[0][0]+self.mati[0][1]+self.mati[0][2]
        b=self.mati[2][0]+self.mati[2][1]+self.mati[2][2]
        c=self.mati[1][0]+self.mati[1][2]
        d=a+b+c
        print(d)
    def sumofrows(self):
        a=self.mati[0][0]+self.mati[0][1]+self.mati[0][2]
        b=self.mati[1][0]+self.mati[1][1]+self.mati[1][2]
        c=self.mati[2][0]+self.mati[2][1]+self.mati[2][2]
        d=a+b+c
        print(a,b,c,"Total is",d)
mat=Matrx()
mat.prntantidia()
mat.sumofbrdrelmnt()
mat.sumofrows()
        