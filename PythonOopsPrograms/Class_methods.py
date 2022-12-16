class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"

# Used to change class Variables using class Method and also
# used to access class variables with the help of both instance and class variables can access.


    @classmethod
    def change_no_of_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

adarsh = Employee("Adarsh vajpayee",30_000,"FrontEnd Developer")
manoj = Employee("Manoj Gouda",25_000,"Business administrator")

Employee.change_no_of_leaves(34)
print(adarsh.no_of_leaves)
print(Employee.no_of_leaves)

# Both adarsh i.e (instance) and  Employee i.e (class) Able to access.

# Mostly class Methods are used to create an alternative constructors.