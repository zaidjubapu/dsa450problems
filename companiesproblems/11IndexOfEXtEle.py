class Solution:
    def findExtra(self,a,b,n):
        '''index=0
        for i in a:
            if i not in b:
                return index
            index+=1'''
        i=0
        while a[i] == b[i]:
            i=i+1
            if i == len(a)-1:
                break
        return i
        
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
