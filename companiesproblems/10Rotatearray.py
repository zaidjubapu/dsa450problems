

class Solution: 
    def rotateArr(self,A,D,N):
        
        '''for j in range(D):
            
            temp = A[0]
            for i in range(N-1):
                A[i]=A[i+1]
                
            A[N-1]=temp'''
            
        '''a=N-D
        z=A[:D]
        A[:a]=A[D:]
        A[a:]=z'''
        
        a=N-D
        i=A[:a]
        A[:D]=A[a:]
        A[D:]=i
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends