class Computer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update(self):
        self.age = 21

    def compare_age(self, other):
        if self.age == other.age:
            return True
        else:
            return False


FPname = input("Enter First Person Name: ")
FPage = int(input("Enter First Person Age: "))
SPname = input("Enter second Person Name: ")
SPage = int(input("Enter second Person Age: "))
TPname = input("Enter Third Person Name: ")
TPage = int(input("Enter Third Person Age: "))

c1 = Computer(FPname, FPage)
c2 = Computer(SPname, SPage)
c3 = Computer(TPname, TPage)

if c1.compare_age(c2):
    print(f"After Comparing {FPname} with{SPname} we get to that they are of same age.")
elif c1.compare_age(c3):
    print(f"After Comparing {FPname} with{TPname} we get to that they are of same age.")
else:
    print(f"there is difference of {abs(c2.age - c1.age)} Years between {c2.name} and {c1.name} .")
    print(f"there is difference of {abs(c3.age - c1.age)} Years between {c3.name} and {c1.name} .")

"""
OUTPUT:

Enter First Person Age: 21
Enter second Person Name: Ashish Vajpayee
Enter second Person Age: 24
Enter Third Person Name: Akansha Vajpayee
Enter Third Person Age: 15
there is difference of 3 Years between Ashish Vajpayee and Adarsh vajpayee .
there is difference of 6 Years between Akansha Vajpayee and Adarsh vajpayee .

"""


