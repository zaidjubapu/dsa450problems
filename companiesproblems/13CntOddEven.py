

class Solution:
	def countOddEven(self, arr, n):
		#Code here
		o=0
		e=0
		for i in arr:
		    if i %2 == 0:
		        e+=1
		    else:
		        o+=1
		print(o,e)
		      
		        


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
    	obj = Solution()
    	obj.countOddEven(arr, n);
