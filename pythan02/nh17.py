n=("hello and welcome to my world")
i=0
c=n.split()
print(c)
print(type(c))
print(type(n))
l2=[]
while i<len(c):
    l2.append(c[i].capitalize())
    i=i+1
print(l2)