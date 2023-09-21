c=int(input("Enter the value"))
if(c<=100):
    print("Rs=0")
elif(c>=100 and c<=200):
    s=(c-100)*5
    print(s)
elif(c>=200):
    f=500+(c-200)*10
    print(f)
else:
    print("Not")
    
       