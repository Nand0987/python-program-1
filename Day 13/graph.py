def adj_List():
    v=int(input("Enter number of vertex"))
    e=int(input("Enter number of edges"))
    l1=[]
    for i in range(0,v):
        l1.append([])
    for i in range(0,e):
        s=int(input("Enter source vertex"))
        d=int(input("Enter destination vertex"))
        l1[s].append(d)
        l1[d].append(s)
    return l1

#How to print adj_List

def printadjList(l1):
    for i in range(len(l1)):
        print(str(i)+"->",end=" ")
        for j in l1[i]:
            print(j,end=" ")
        print()


l1=adj_List()
printadjList(l1)


   
      





