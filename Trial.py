from collections import deque
class Node :
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None


def createBinaryTree(l1):
    if len(l1)==0:
        return None
    else:
        d1=deque()
        root=Node(l1[0])
        d1.append(root)
        i=1
        while len(l1)>i:
            if(l1[i]==None):
            
                if(i%2==0):
                    d1.popleft()
            
            else :

                n=Node(l1[i])
                if(i%2==0):
                    d1[0].right=n
                    d1.append(n)
                    d1.popleft()
                else :
                    d1[0].left=n
                    d1.append(n)
            i+=1
    return root            

def inOrder(root):
    if(root !=None):
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
    else:
        return ;



root=createBinaryTree([4,3,5,7,None,8])
inOrder(root)