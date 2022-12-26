def Remove_Duplicate(Values):
    return list(dict.fromkeys(Values))
myobj=Remove_Duplicate([1,2,3,4,5,4,3,2,1])
print(myobj)
