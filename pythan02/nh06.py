z=int(input(""))
i=2
count=1
while(i<=z//2):
    if(z%i==0):
        count+=1
    i=i+1

if count==1:
    print("prime")
else:
    print("not prime") 