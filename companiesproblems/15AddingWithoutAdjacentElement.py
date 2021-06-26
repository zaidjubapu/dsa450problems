
class Solution:
	
	def findMaxSum(self,arr, n):
	    if n ==1:
	        return arr[0]
	        
	    if n == 2:
	        return max(arr[0],arr[1])
        
        incl = arr[0]
        excl = 0
        for i in range(1,n):
            incl1=incl
            incl  = arr[i]+excl
            excl = max(incl1,excl)
            
        return max(incl,excl)
		
		        




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1
