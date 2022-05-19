

'''def reverseWord(s):
    a=[]
    a[:0] = s # creating list of string characters
    for i in range(int(len(s)/2)):
        a[i],a[len(s)-i-1]=a[len(s)-i-1],a[i]
    
    b="".join(a)
    return b
        
        

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1'''
'''def reversWord(s):
    a=[]
    a[:0] = s
    for i in range(int(len(a)/2)):
        a[i],a[len(s)-1-i]=a[len(s)-1-i],a[i]

    print(a)
    b="".join(a)
    a.pop()
    v=a.reverse()
    print(v)
    return b



a=input("enter the workd")
print(reversWord(a))
d=reversWord(a)
#s=d.split("")
#print(s)'''


a=[1,2,38,2,1,]
a.sort()
print(a)
z=a.reverse()
print(a)


