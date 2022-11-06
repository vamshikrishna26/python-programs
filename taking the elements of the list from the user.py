list=[]
size_of_list=int(input("enter the size of the list : "))
for i in range(0,size_of_list):
    list.append(input("insert elements in the list : "))
print("printing the elements in the list : ")
for i in list:
    print(i,end="  ")