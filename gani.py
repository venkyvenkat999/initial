"""def fun(l,i):
    if(l[i]%2==0 and i!=len(l)):
        m.append(l[i])
    else:
        if(i!=len(l)):
            p.append(l[i])
    i=i+1
    return fun(l,i)
l=list(map(int,input().split(",")))
p=[]
m=[]
k=fun(l,0)
print(m,p,k)
"""
def fun(l,i,e,o):
    while(i<len(l)):
        if(l[i]%2==0):
            e.append(l[i])
        else:
            o.append(l[i])
        i=i+1
    return (e,o)
e=o=[]
l=list(map(int,input().split(",")))
print(fun(l,0,e,o))
"""
i=0
while(True):
    if(i==0):
        print("hello")
        break
"""