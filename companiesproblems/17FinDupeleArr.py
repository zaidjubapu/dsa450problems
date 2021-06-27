
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	'''arr1=[]
    	arr2=arr.copy()
        for i in range(n):
            p = arr2.pop(0)
            if p in arr2:
                if p in arr1:
                    continue
                else:
                    arr1.append(p)
                    
        if len(arr1) == 0:
            arr1.append(-1)
            return arr1
        else :
            a = arr1.sort()
            return arr1'''
    	for i in range(0, n):
            index = arr[i] % n
            arr[index] += n

        # Now check which value
            # exists more
        # than once by dividing
            # with the size
        # of array
        arr1=[]
        for i in range(0, n):
            if (arr[i]/n) >= 2:
                #print(i, end=" ")
                a=arr[i]/n
                arr1.append(i)
        
        if len(arr1) == 0:
            arr1.append(-1)
            return arr1
        else :
            a = arr1.sort()
            return arr1

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()


