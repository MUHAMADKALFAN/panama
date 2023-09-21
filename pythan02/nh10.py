l1=[]
l2=[]
l3=[]
i=0
z=0
j=0
while(z<5):
# for i in range(5):
    x=int(input("Enter No L1:"))
    l1.append(x)
    z=z+1

while(j<5):
        t=int(input("Enter No L2:"))
        l2.append(t)
        j=j+1
print(l1)
print(l2)

while(i<5):
    if(l1[i] in l2):
        l3.append(l1[i])
    i=i+1
print(l3)   