"""
l=[2,2,3,3]
can=5
for i in l:
    while(can>=i):
        
n=int(input("enter the n value:"))
k=int(input("k value:"))
l=list(map(int,input().split(" ")))
s=l[-k:]+l[:-k]
print(*s)
"""
s=input("enter the string :")
l=[]
p=[]
for i in range(97,123):
    l.append(chr(i))
for i in range(len(s)):
    if(s[i]==" "):
        pass
    else:
        if s[i].lower() not in p:
            p.append(s[i].lower())
p.sort()
print(p)
if(len(p)==len(l)):
    print("pangram")
else:
    print("not pangram")
