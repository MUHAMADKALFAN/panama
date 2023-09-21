n=int(input("Enter a number: "))
i=0
# # while(i<=n): 
# #        j=2
# while(j<=n): 
#     if(i%j==0): 
#         break 
#     j+=1 
#     if(i==j): 
#         print("*",end=' ') 
        # i+=1
while (i<=10):
    j=0
    while(j<=i+1):
        print("*",end=" ")
        j=j+1
    print()
    i=i+1