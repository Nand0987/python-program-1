def adj_matrix_implementation():
    v=int(input("Enter number of vertex"))
    e=int(input("Enter number of edges"))
    adj_matrix=[[0 for i in range(v)] for i in range(v)]
    for i in range(e):
        s=int(input("Enter source vertex"))
        d=int(input("Enter destination vertex"))
        adj_matrix[s][d]=1
        adj_matrix[d][s]=1
    return adj_matrix
    
adj_matrix=adj_matrix_implementation()
print(adj_matrix)
        
#How to make V*v matrix and fillup with values 0
# adj_matrix=[]
# temp=[]
# for i in range(3):  #[0,0,0]
#     temp.append(0)
# for i in range(3):
#     adj_matrix.append(temp)
# print(adj_matrix)

# temp=[0 for i in range(3)] [0,0,0]
# print(temp)

# adj_matrix=[[0 for i in range(3)] for i in range(3)]
# print(adj_matrix)

