s=input("Enter a string")
print(s)
a=len(s)
print(a)
count=0
for i in s:
    if i==' ':
        count+=1
print("Number of spaces",count)
print("Number of words",count+1)
d=s.split(' ')
print(d)
for word in d:
    if len(word)%2==0:
        print(word)

