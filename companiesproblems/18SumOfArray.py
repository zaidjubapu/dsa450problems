

class Solution:
    def getSum(self, arr, n):
        # Your code goes here
        return sum(arr)
    
    



def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.getSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } 