# n="An assault rifle in decent condition"
n=input("Enter the:-")
l1=[]
x=n.split()
print(x)
i=0
while(i<len(x)):
    if(len(x[i])>=5):
        l1.append(x[i])
    i=i+1
print(l1)

