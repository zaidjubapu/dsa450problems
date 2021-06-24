
class Solution:
    def sort012(self,arr,n):
        '''for i in range(n-1):
            for j in range(n-1-i):
                if arr[j] > arr[j+1]: 
                    arr[j],arr[j+1] = arr[j+1],arr[j]'''
                    
        low = 0
        high =n-1
        mid = 0
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low = low +1
                mid= mid +1
                
            elif arr[mid] == 1:
                mid = mid +1
                
            else:
                arr[mid],arr[high]=arr[high],arr[mid]
                high = high -1
                
        


if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()
