arr=[2,0,1,2,0]
n=len(arr)

low = 0
high = n-1
mid=0


while mid <= high:
    if arr[mid]==0:
        arr[low],arr[mid] = arr[mid],arr[low]
        low = low + 1
        mid = mid + 1

    elif arr[mid] == 1:
        mid = mid + 1

    else:
        arr[mid],arr[high] = arr[high],arr[mid]
        high = high - 1

print(arr)


arr =  [4,5,6,4,5]
n=len(arr)

low = 0
mid = 0 
high = n - 1

while mid<= high:
    if arr[mid] == 4:
        arr[mid],arr[low]=arr[low],arr[mid]

    elif arr[mid] == 5:
        mid = mid + 1

    else :
        arr[high],arr[mid]=arr[mid],arr[high]
        high = high - 1

print(arr)



    




