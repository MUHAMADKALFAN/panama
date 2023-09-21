n=int(input("Enter the No:"))
# i=2
count=1
# if n>1:
for i in range(2,n):
     if(n%i==0):
        count=0  
        break
if (count==1):      
    print("prime")
else:
        print("not prime") 