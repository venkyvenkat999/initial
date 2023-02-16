"""
x=[int(x) for x in input().split(" ")]
print("".join(str(x)))
def evenOdd(x):
     
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code to call the function
print(evenOdd.__doc__)

def square_value(*argv):
    for i in argv:
        print(i**2,end=" ")
 
 
square_value(2,3,4,5,6)
#function with many arguments
def dic(**kwargs):
    for key,value in kwargs.items():
        print("%s:%s" %(key,value))
dic(first='hii',mid='guvi',last='jaan')
#lambda function and normal function 
def cube(n):
    return n*n*n
cube_val=lambda x,y:x*y
print(cube(7))
print(cube_val(7,5))
#join function
l=['a','b','c','d']
print(" ".join(l))
print(6,7,8,sep='+')# separator 
print("geeks for geeks"),
print("python")
print('g','f','g',sep='+')
print(5)
l1=[2,3,4,5]
l2=l1.copy()
print(l1,l2)
l2.append(8)
print(l1,l2)
# new program
l1=[1,2,3,4]
l2=l1
print(l1,l2)
l1.append(6)
print(l1,l2)
l1.remove(1)
l1.pop(0)
print(l1,l2)
#del l1[2]
#del l1 removes list when we try to  print it it will give error
#l1.clear() this also clears the entire list but when we print it will give empty list
thislist = ["apple", "banana", "cherry"]
[print(f'"{x}"') for x in thislist]#main code usefull code
"""
#to print list values in double quotes
#new program
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
[print(f'"{x}"',end=" ") for x in list1]


print(list1)
print(list2)
print(list3)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "pass" for x in fruits]

print(newlist)
fruits=['hii','hello']
print(fruits.count("hii"))#no of times hii is repeated