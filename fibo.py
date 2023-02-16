def f(n):
    if(n<0):
        return -1
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
n=int(input("enter the no.of fibo numbers you want"))
for i in range(n):
    print(f(i),end=" ")