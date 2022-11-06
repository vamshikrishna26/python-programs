list=[1,1,2,3,4,3,4,2,5,4,7,655,43,54,34,43]
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)