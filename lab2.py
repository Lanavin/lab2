a = [1,5,14,20,23,24,-8, -4]
print (a)
b=a[0]
for i in range (len(a)):
    if b>a[i]:
        b=a[i]
print (b)

c=0
for i in range (len(a)):
   c = c+a[i]

print (c)
d=c/len(a)
print(d)

print(sum(a)/len(a))