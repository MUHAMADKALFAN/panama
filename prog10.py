z=input("Enter the number of:")
h={31:"Janu,Mar,May,Jul,Aug,Oct,Dec",30:"Apr,Jun,Sep,Nov",28:"Feb",29:"Feb"}
if(z in h[31]):
    print("31")
elif(z in h[30]):
    print("30")
elif(z in h[28]):
    print("28")
elif(z in h[29]):
    print("29")
else:
    print("not")
