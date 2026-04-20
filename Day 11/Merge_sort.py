# def merge(arr,l,m,r):
#     l1=[]
#     l2=[]
#     for i in range(l,m+1):
#         l1.append(arr[i])
#     for i in range(m+1,r+1):
#         l2.append(arr[i])
#     i=0
#     j=0
#     k=l
#     while(len(l1)>i and len(l2)>j):
#         if(l1[i]>l2[j]):
#             arr[k]=l2[j]
#             j+=1
#             k+=1
#         elif(l1[i]<l2[j]):
#             arr[k]=l1[i]
#             i+=1
#             k+=1
#         else :
#             arr[k]=l1[i]
#             i+=1
#             k+=1
#             arr[k]=l2[j]
#             j+=1
#             k+=1
    

# def merge_sort(arr,l,r):
#     if(l<r):
#         m=(l+r)//2
#         merge_sort(arr,l,m)
#         merge_sort(arr,m+1,r)
#         merge(arr,l,m,r)


# merge_sort([7,5,4,3],0,3)
# # merge([2,3,5,7,4,9,12,14],0,3,7)


from collections import deque
q=deque()
q.append(10)
q.append(20)
q.append(30)
q.popleft()
print(q[0])