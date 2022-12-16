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

adarsh = Employee("Adarsh", "Vajpayee")
gnanesh = Employee("Gnanesh", "Auti")


print(adarsh.email)

adarsh.fname = "Aditya"
# print(adarsh.explain())
print(adarsh.email)

adarsh.email = "this.that@gmail.com"

print(adarsh.fname)
print(adarsh.lname)
print(adarsh.email)

# it is finding a deleter to delete it.
del adarsh.email

print(adarsh.email)

