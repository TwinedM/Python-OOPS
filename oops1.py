# This would cover all the basics of oops
# inititate a class
class employee:
    # use dunder method for a constructor """ 
    def __init__(self):
        print(id(self))
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
    def travel(self,designation):
        print(f"They are going to {designation}")
# creating object of class

sam = employee()
print(id(sam))




