l=list(map(int,input("Enter Numbers of a list:").split()))
e=int(input("Enter the element to delete:"))
for i in range(0,len(l)):
    if(l[i]==e):
        for j in range(i,len(l)-1):
            l[j]=l[j+1]
        l[j+1]=None
if l[-1]==None:
    l.remove(l[-1])
print(l)
