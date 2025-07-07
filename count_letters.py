# String input
input_count=input("enter sentence for counting :\n")

counter=0

for i in input_count:
    if i==" ":
        continue
    else:
        counter+=1
        
     
print(counter)