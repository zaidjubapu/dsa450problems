
class Solution:
    def countZeroes(self, arr, n):
        # code here
        a=arr.index(0)
        return len(arr)-a


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr, n)
        print(ans)
        tc -= 1

