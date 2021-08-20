#create a dictonary from user input find the biggest value and show key
freq = {}
total_no_of_item=int(input("enter total no of your iteam"))
for i in range(total_no_of_item):
    b=input("input only iteam name sequencely")
    print(f"enter total number of",b)
    c=int(input("enter here \t"))
    if b not in freq:
        freq[b]=c
key_list=list(freq.keys())
val_list=list(freq.values())
count=0
for i in val_list:
    if i >count:
        count=i
ind=val_list.index(count)
print(key_list[ind])
        

