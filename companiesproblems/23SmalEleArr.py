
def countOfElements( a, n, x):
    
    c=0
    for i in range(n):
        if a[i] <= x:
            c+=1
            
    return c
    





def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        print(countOfElements(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

