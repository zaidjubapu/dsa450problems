

def reverseWord(s):
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
        t = t-1

