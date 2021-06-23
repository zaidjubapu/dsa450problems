


def calculate (a, n) : 
    #Complete the function
    ##def calculate(a) :
 
    # Sorting the list using
    # built in function
    a.sort()
     
    count = 1
    answer = 0
     
    # Traversing through the elements
    for i in range(0, len(a)-1) :
 
        if a[i] == a[i + 1] :
             
            # Counting frequncy of each elements
            count += 1
 
        else :
 
            # Adding the contribution of
            # the frequency to the answer
            answer = answer + count * (count - 1) // 2
            count = 1
 
    answer = answer + count * (count - 1) // 2
     
    return answer
    


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = calculate(arr, n)
    print(res)
