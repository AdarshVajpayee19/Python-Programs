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

    # Special Methods
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return  other.salary / self.salary

    # print(emp1) properly instead of this -->  <__main__.Employee object at 0x00000196D9267E20>
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    # to define about object.
    def __str__(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"

emp1 = Employee("Adarsh Vajpayee", 45_000, "Web developer")
emp2 = Employee("Gopal Krishna", 75_000, "DeveOps Engineer")

print(emp1 + emp2)
print(emp1 / emp2)

# Want More Than Search 'Mapping Operators to Functions'.
# Dunder Methods

# if str is not present print karne paar bhi repr dikhayega aur str karne pe bhi repr dikhayega if expicitly repr likne pe repr chalega.

print(emp1)
print(repr(emp1))
