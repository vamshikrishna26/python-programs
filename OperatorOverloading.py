class Operator_Overloading:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return Operator_Overloading(self.a+other.a,self.b+other.b)

    def __lt__(self, other):
        if self.a+other.a < self.b+other.b:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.a+other.a>self.b+other.b:
            return True
        else:
            return False



obj1=Operator_Overloading(10,20)
obj2=Operator_Overloading(30,40)
obj3=obj1+obj2
print(obj3)
print(obj3.a)
print(obj3.b)
print(obj1<obj2)
print(obj1>obj2)