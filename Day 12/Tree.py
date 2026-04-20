#create Node
from collections import deque
class Node :
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
    
def createTree(l1):
    if len(l1)==0 :
        return None
    else :
        root=Node(l1[0])
        d1=deque()
        d1.append(root)
        i=1
        while len(l1)>i:
         if l1[i]!=None :
            if i%2==0 :
                n1=Node(l1[i])
                d1[0].right=n1
                d1.append(n1)
                d1.popleft()
            else :
                n1=Node(l1[i])
                d1[0].left=n1
                d1.append(n1)
         i+=1
    return root





root=createTree([1,2,3,None,4,None,5])