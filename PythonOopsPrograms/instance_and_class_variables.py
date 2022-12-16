class Employee:
    no_of_leaves = 8
    pass

adarsh = Employee()
manoj = Employee()

adarsh.name = "Adarsh vajpayee"
adarsh.salary = "30_000"
adarsh.role = "FrontEnd Developer"

manoj.name = "Manoj Gouda"
manoj.salary = "25_000"
manoj.role = "Business administrator"

manoj.no_of_leaves = 20

print(manoj.no_of_leaves) # 20
print(adarsh.no_of_leaves) # 8

print(Employee.no_of_leaves) # 8
print(Employee.__dict__)
Employee.no_of_leaves = 10
print(Employee.__dict__)
print(Employee.no_of_leaves)

# We cannot Change the class variable with the help of instance variable.