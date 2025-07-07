# **enter number and check Prime number or no

# get input
x=int(input("Enter number: \n"))

count=0 
# loop reapeat 2 to the input
for i in range(2,x):
    
    if x%i==0:
        count+=1


if count>=1:
    print("No")

else:
    print("yes,Aval")