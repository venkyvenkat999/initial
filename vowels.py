n=input("enter the string:")
n=set(n)
d=list(n)
l=['a','e','i','o','u','A','E','I','O','U']
p=[]
count=0
for i in range(len(d)):
    if((d[i].lower() or d[i].upper()) in l):
        count+=1
        continue
    else:
        p.append(d[i])
if(count==5):
    print("accepted")
else:
    print("not accepted")
    print("not in string",*p)