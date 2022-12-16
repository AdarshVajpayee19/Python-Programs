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
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        # one-liner
        return cls(*string.split("-"))


adarsh = Employee("Adarsh vajpayee",30_000,"FrontEnd Developer")
manoj = Employee("Manoj Gouda",25_000,"Business administrator")
# Alternative Constructor with only one parameter.
gopal = Employee.from_str("Gopal Krishna-42_000-deveops")

print(gopal.salary)
Employee.change_no_of_leaves(34)
# print(adarsh.no_of_leaves)
# print(Employee.no_of_leaves)

