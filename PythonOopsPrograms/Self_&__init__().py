class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"


adarsh = Employee("Adarsh vajpayee",30_000,"FrontEnd Developer")
manoj = Employee("Manoj Gouda",25_000,"Business administrator")

# adarsh.name = "Adarsh vajpayee"
# adarsh.salary = "30_000"
# adarsh.role = "FrontEnd Developer"
#
# manoj.name = "Manoj Gouda"
# manoj.salary = "25_000"
# manoj.role = "Business administrator"

# Instead Create Constructor __init()__ to initialize object variables.

print(adarsh.printdetails())
print(manoj.printdetails())

