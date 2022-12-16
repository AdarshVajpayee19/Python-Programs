# Getting to know about the details of object from where it comes from,
# and getting infomation, and knowing how it get stored, getting information
# is nothing  Object IntroSpection.


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}{lname}19@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}."

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set,please set it using Setter."
        return f"{self.fname}.{self.lname}@gmail.com"

    # To set email Attributes
    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("Skill","F")
print(skillf.email)
print(type(skillf))

print(id("Adarsh Vajpayee"))
print(id("Ashish Vajpayee"))
# 2439554596464
# 2439554613552
# u can see they have Different id.

o = "this is string"
print(dir(o))
print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))
