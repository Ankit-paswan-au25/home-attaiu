#swapping in array in array elements and making it reverse
a=[]
usrip=int(input("entterr the length of array"))
for i in range(usrip):
    usrip1=int(input("enter element"))
    a.append(usrip1)

f=int(len(a)/2)
print(f)
#a[0],a[-1]=a[-1],a[0]
#a[1],a[-2]=a[-2],a[1]
print("before reversing array",a)
b=-1
for i in range(f):
    a[i],a[b]=a[b],a[i]
    b=b-1
print("after reversing array",a)