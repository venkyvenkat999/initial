"""s="good morning india!"
s=s.replace(" ","")
for i in range(len(s)):
    if(s[i] in s[i+1:]):
        pass
    else:
        print(s[i])
        break
"""
"""
#a=0,b=1,c=2---etc
#To print the sum of characters in a string 
s="rama"
l=[]
s=s.upper()
for i in range(len(s)):
    l.append((ord(s[i])-65))
print(sum(l))
#to print the nearest prime number to given number
import math
n=27
l=[]
for i in range(2,n+1):
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0 and i!=2):
            break
    else:
        l.append(i)
print(l[-1])
#main code
def is_even(number):
  message =  f"{number} is an even number" if number % 2 == 0 else  f"{number} is an odd number"
 return message
print(is_even(54))
#reverse the key value pairs
d={"hello":"world","first:1}
e={val:k for k,val in a.items()}
print(e)
#odd position lower letter and even position upper letter 
word = "Python Programming"
n = len(word)
word1 = word.upper()
word2 = word.lower()
converted_word = ""
for i in range(n):
 if i % 2 == 0:
   converted_word += word2[i]
 else:
   converted_word += word1[i]
print(converted_word)
#only elements not in list b
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = [x for x in a if x not in b]
print(c)
"""
#binary search
def binarySearch(low,high,l,n):
    if(low<=high):
        mid=(low+high)//2
        if(l[mid]==n):
            return mid
        elif(l[mid]>n):
            return binarySearch(low,mid-1,l,n)
        elif(l[mid]<n):
            return binarySearch(mid+1,high,l,n)
        else:
            return -1
    else:
        return -1
l=[1,2,3,4,5,8,6,9]
l.sort()
p=len(l)-1
print(binarySearch(0,p,l,9))