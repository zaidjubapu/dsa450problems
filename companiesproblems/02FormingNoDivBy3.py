

class Solution:
    def isPossible(self, N, arr):
        # code here
        if sum(arr)%3 == 0:
            return 1
        else:
            return 0



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code End