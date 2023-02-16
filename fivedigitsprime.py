import math
count=0
l=[]
m=int(input("enter the first digit:"))
n=int(input("enter the second digit:"))
for i in range(m,n):
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            count+=1
            break
    else:
        l.append(i)
print(max(l),min(l))
