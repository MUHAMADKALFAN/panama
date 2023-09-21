z=int(input("Enter the number of:"))
h={31:"Janu,Mar,May,Jul,Aug,Oct,Dec",30:"Apr,Jun,Sep,Nov",28:"Feb",29:"Feb"}
if(z==31):
    print(h[31])
elif(z==30):
    print(h[30])
elif(z==28):
    print(h[28])
elif(z==29):
    print(h[29])
else:
    print("not")



