

class Solution:

    def leaders(self, A, N):
        #Code here
        '''arr=[]
        for i in range(len(A)-1):
            if A[i]>=A[i+1]:
                c=max(A[i+1:N])
                if c > A[i]:
                    continue
                else:
                    arr.append(A[i])
                    
        arr.append(A[N-1])
        return arr'''
        temp = []
        lt = A[N-1]
        temp.append(lt)
        for i in range(N-2,-1,-1):
            if lt <= A[i]:
                temp.append(A[i])
                lt=A[i]
                
        temp=temp[::-1]
        
        return temp


import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
