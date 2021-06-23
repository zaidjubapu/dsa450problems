

class Solution:
	def swapElements(self, arr, n):
		temp = 0
        for i in range(len(arr)-2):
            temp = arr[i]
            arr[i]=arr[i+2]
            arr[i+2]=temp


		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
    	obj = Solution()
    	obj.swapElements(arr, n);
    	for i in arr:
    	    print(i, end = " ")
    	print()