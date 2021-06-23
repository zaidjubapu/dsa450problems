
class Solution:

	def findMaximum(self,arr, n):
		maxx = 0
		i=0
		while (arr[i]>=maxx):
		    maxx = arr[i]
		    i=i+1
		    if i == n:
		        break
		    
		return maxx







if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1
