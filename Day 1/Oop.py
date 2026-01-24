#dict is a class
# d1={102:"rahul",105:"nitish",106:"Arjun"}
# print(d1)
# d1={} #empty dict
# print(d1)
# d1=dict(a=10,b=20,c=30)
# print(d1)
# d1=dict("102":"rahul")
# print(d1)
# d1=dict(a=10,b=20,c=30)
# print(type(d1))
#How to access element in dict
# d1={102:'nitish',104:'rahul',105:'harshit'}
# print(d1)
# print(d1[104])
# print(d1[105])
# print(d1[105],d1[104])
# for k in d1:
#     print(k) #print only keys

# for k in d1:
#     print(k,d1[k])

#why while loop is not applicable

#How to edit dict element
# d1={102:'nitish',104:'rahul',105:'harshit'}
# d1[104]='roushan'
# print(d1)
#notes : we can change only values not keys

#How to add element in the dict
# d1={102:'nitish',104:'rahul',105:'harshit'}
# d1[106]='ritish'
# print(d1)

#methods : items(),values(),keys()
#  items() : collections of elements
# d1={102:'nitish',104:'rahul',105:'harshit'}
# print(d1.items())
# [(102, 'nitish'), (104, 'rahul'), (105, 'harshit')]
# for k in d1.items():
#     print(k[0],k[1])
# [(102, 'nitish'), (104, 'rahul'), (105, 'harshit')]
# d1=d1.items()
# d1=list(d1)

# i=0
# while len(d1)>i:
#     print(d1[i])
#     i+=1

# note applicable comparision operator > , < ,>= ,<= 
#== != supported
# d1={102:'rahul',103:'nitish'}
# d2={103:'nitish',102:'rahul'}
# print(d1==d2)
#order not importent

#pop(key):
# d1={102:'nitish',104:'rahul',105:'harshit'}
# d1.pop(102)
# print(d1)
# del d1[102]
# print(d1)

#popitem()
# d1.popitem()
# print(d1)
# d1.clear()
# print(d1) delete all element





