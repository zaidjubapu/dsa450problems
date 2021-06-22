
class Solution:
    def segregate0and1(self, arr, n):
        low = 0
        high = len(arr)-1
        while (low <= high):
            if arr[low] == 0:
                low = low +1
            else:
                arr[low],arr[high]=arr[high],arr[low]
                high = high -1
        return arr
                


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregate0and1(arr, n)
        print(*arr)
        tc -= 1

