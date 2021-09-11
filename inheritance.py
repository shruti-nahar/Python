class person:
    def accept(self):
        self.name=input("enter a name")
        self.age=int(input("enter a age"))
        self.address=input("enter your address")
    def display(self):
        print("your name is",self.name,"your age is",self.age,"your address is",self.address)
class employee(person):
    def salary(self):
       self.salary=int(input("enter a salary"))
       
    def dispsalary(self):
        print("salary is ",self.salary)
class student(person):
    def percentage(self):
        self.percent=int(input("enter a percentage"))
    def disppercentage(self):
        print("percentage is ",self.percent)
obj=employee()
obj.accept()
obj.display()
obj.salary()
obj.dispsalary()
obj2=student()
obj2.accept()
obj2.display()
obj2.percentage()
obj2.disppercentage()

                        
