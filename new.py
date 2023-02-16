str_value="venkatesh"
new_list = [char for char in str_value.lower() if char in 'aeiou']
print(new_list)
ar1=list(map(int,input().split(",")))
ar2=list(map(int,input().split(",")))
ar3=list(map(int,input().split(",")))
ar1=set(ar1)
ar2=set(ar2)
ar3=set(ar3)
set1=ar1.intersection(ar2)
final=set1.intersection(ar3)
print(list(final))