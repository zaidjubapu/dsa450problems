

class Solution:
       
    def maxSubArraySum(self,a,size):
        
         maxSoFar=0;
         maxEndHere=0;
         
         for i in range(len(a)):
             maxEndHere = maxEndHere+a[i]
             if maxEndHere < 0:
                 maxEndHere =0
             if maxEndHere > maxSoFar:
                 maxSoFar= maxEndHere
         return maxSoFar


import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
