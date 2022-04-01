a=[1,5,3,2,6]
for i in range(int(len(a)/2)):
    a[i],a[len(a)-i-1] = a[len(a)-i-1],a[i]

print(a)
