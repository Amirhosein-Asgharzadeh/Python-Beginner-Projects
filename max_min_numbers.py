# 3 input
a=int(input("Enter 3 Numbers:\n"))
b=int(input())
c=int(input())

# Find a Maximum Number
if a>b and a>c:
    print("max= ",a)
elif b>c:
    print("max= ",b)
else:
    print("max= ",c)


# Find a Minimum Number
if a<b and a<c:
    print("min= ",a)   
elif b<c:
    print("min= ",b)
else:
    print("min= ",c)



