l1=("delhi","kol","jaipur","guru","patna")
# print(l1[0])
# print(l1[len(l1)-1])

i=0
while len(l1)-1>=i:
    if(l1[i]=="delhi"):
        print("delhi exist")
        break
    i+=1
if(len(l1)==i):
 print("delhi not exist")