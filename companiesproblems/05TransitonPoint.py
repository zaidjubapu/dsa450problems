
def transitionPoint(arr, n):
    for i in range(n):
        if arr[i] == 1:
            return i
            
    return -1
            

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

