def binarySearch(arr, target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(target==arr[mid]):
            return mid
        elif(target > arr[mid]):
            low=mid+1
        else:
            high=mid-1
    return -1

