class Solution:
    
    def countBuildings(self,h, n):
        # code here
        arr=h
        c=1
        maxx = arr[0]
        for i in range(1,n):
            if arr[i] > maxx:
                maxx=arr[i]
                c = c+1
                
        return c
                

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        h = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(h, n)
        print(ans)
        tc -= 1
