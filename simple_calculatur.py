"""Press the "Enter" key after each input
*example: 
         2
         +
         3
         *
         2
         =
        (*Anser)"""


r=int(input("Enter Number:\n"))

# if input =="=" loop is break
while True:

    j=input()

    if j=="=":
        break

    num=int(input())

    if j=="+":
        r+=num
    if j=="-":
        r-=num

    if j=="*":
        r*=num

    if j=="/":
        r/=num


print("--------------------------------")    
print("*Anser=  ")
print(r)
