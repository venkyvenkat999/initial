"""stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop(1)
print(stack)
print(len(stack)==0)

#creation of a stack using list
l=[]
def push():
    p=int(input("enter the element you want to push:"))
    l.append(p)
    print(l)
def pop():
    if not l:
        print("stack is empty")
    else:
        e=l.pop()
        print("the element you pop is",e)
        print(l)
while True:
    choice=int(input("enter your choice:"))
    if(choice==1):
        push()
    elif(choice==2):
        pop()
    elif(choice==3):
        break
    else:
        print("the element you enter is invalid")

# implementation of stack using deque class
import collections 
stack=collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
"""
#stack using lifo queue
import queue
stack=queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
print(stack)