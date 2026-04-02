def merge_two_sorted_array(arr1,arr2):
    ans=[]
    i=0
    j=0
    while(len(arr1)>i and len(arr2)>j):
        if(arr1[i]<arr2[j]):
            ans.append(arr1[i])
            i+=1
        elif(arr1[i]>arr2[j]):
            ans.append(arr2[j])
            j+=1
        else :
            ans.append(arr1[i])
            ans.append(arr2[j])
            i+=1
            j+=1
          
    while(len(arr1)>i):
        ans.append(arr1[i])
        i+=1
    while(len(arr2)>j):
        ans.append(arr2[j])
        j+=1
    return ans


print(merge_two_sorted_array([10,20,30,40,50,60,70],[15,20,25,30,45]))