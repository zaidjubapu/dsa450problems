

class Solution:    
    
    def doUnion(self,a,n,b,m):
        
        c=b
        for i in a:
            if i not in b:
                c.append(i)
                
        d=set(c)
        return len(d)
                


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
