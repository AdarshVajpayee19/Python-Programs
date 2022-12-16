class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_no_of_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is Good ",string)

class programmer(Employee):
    #we need avoid rewriting of code but for now i am writing without considering it.
    # instead we can use super.
    no_of_holiday = 56
    def __init__(self,aname,asalary,arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printProg(self):
        return f"The programmer's Name is {self.name}. salary is {self.salary} and role is {self.role} The languages are {self.languages}"

adarsh = Employee("Adarsh vajpayee",30_000,"FrontEnd Developer")
manoj = Employee("Manoj Gouda",25_000,"Business administrator")

shabri = programmer("Shabarish", 55_000,"Programmer",["C,c++"])
gopal = programmer("Gopal Krishna", 75_000,"Coder",["Python,Java"])
# print(shabri.printProg())
# print(shabri.printdetails())

print(gopal.printProg())
print(gopal.printdetails())
print(gopal.no_of_holiday)

