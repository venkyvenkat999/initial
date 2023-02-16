key=input("enter the key:")
message=input("enter the message input:")
p=[]
l=[]
output=[]
for i in range(len(key)):
    if key[i] not in p and key[i]!=" ":
        p.append(key[i])
for i in range(97,123):
    l.append(chr(i))
for i in range(len(message)):
    if(message[i] in p and message[i]!=" "):
        m=p.index(message[i])
        output.append(l[m])
    if(message[i]==" "):
        output.append(" ")
print(output)