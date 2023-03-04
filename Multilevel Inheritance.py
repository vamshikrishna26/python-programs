class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
class Father(Grandfather):
    def __init__(self,fathername,grandfathername):
        self.fathername=fathername
        Grandfather.__init__(self,grandfathername)
class Child(Father):
    def __init__(self,childname,fathername,grandfathername):
        self.childname=childname
        Father.__init__(self,fathername,grandfathername)

    def print_name(self):
        print(self.grandfathername)
        print(self.fathername)
        print(self.childname)

obj1=Child("Vamshi","krishna","yadav")

obj1.print_name()
