class Employee:
    no_of_leaves = 8
    var = 500
    _protec = 10
    __private = 99

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_no_of_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
        return cls.no_of_leaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is Good ",string)

emp = Employee("Adarsh V", 45_000," Frond End Developer.")
emp2 = Employee.from_str("Gopal Krishna-50_000-Deveops")
print(emp.printdetails())
print(emp.change_no_of_leaves(35))
print(f"Name is {emp2.name} salary is {emp2.salary} and role is  {emp2.role}.")
print(emp._protec)
# print(emp.__private) #Error
print(emp._Employee__private) #  called 'Name Angling'

