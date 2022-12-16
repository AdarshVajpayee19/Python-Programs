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

adarsh = Employee("Adarsh vajpayee",30_000,"FrontEnd Developer")
manoj = Employee("Manoj Gouda",25_000,"Business administrator")
gopal = Employee.from_str("Gopal Krishna-42_000-deveops")

gopal.printgood("Adarsh")


