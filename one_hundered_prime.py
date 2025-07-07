#  print 100 Prime numbers

num=list(range(1,101))

for iter in num:
    count=0
    # iter=10  >> 10%1=0   10%2=0   10%3   10%4  10%5=0  10%6   10%7  10%8  10%9   10%10=0    count=4  >> NO
    for i in num:
        if iter%i==0:
            count+=1
    if count<=2:
        print(iter)        
