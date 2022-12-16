# TYPES OF Methods:

# 1.Class Methods.
# 2.Static Methods.
# 3. Instance Methods.

# imp_NOTE: Class Variable and Static Variable Are same But Class methods and static methods are different.
# When We are not bother of using variables ie. class variables,static variables, instances variables then we can write a method
# called Static Methods.

class Student:
    College = "BNMIT"

    def __init__(self, name, usn, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # u can use Constructor or u can Use Getters Methods(Actuators) because they only get or initialize value and Setters methods(Mutators)because they change the value.

    def get_m1(self):
        return self.m1

    def set_m1(self, m1):
        self.m1 = m1

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def get_college(cls):
        return cls.College

    @staticmethod
    def exit_info():
        print("************* Bhaago class khatam hogaya ***************")


print(f"******************      {Student.get_college()}      ******************\n")
FPname = input("Enter First Person Name: ")
FPusn = input("Enter First Person usn: ")
FPm1 = int(input("Enter First Person Marks1 : "))
FPm2 = int(input("Enter First Person Marks2 : "))
FPm3 = int(input("Enter First Person Marks3 : "))

SPname = input("\nEnter second Person Name: ")
SPusn = input("Enter second Person usn: ")
SPm1 = int(input("Enter Second Person Marks1 : "))
SPm2 = int(input("Enter Second Person Marks2 : "))
SPm3 = int(input("Enter Second Person Marks3 : "))


TPname = input("\nEnter Third Person Name: ")
TPusn = input("Enter Third Person usn: ")
TPm1 = int(input("Enter Third Person Marks1 : "))
TPm2 = int(input("Enter Third Person Marks2 : "))
TPm3 = int(input("Enter Third Person Marks3 : "))

s1 = Student(FPname,FPusn,FPm1,FPm2,FPm3)
s2 = Student(SPname,SPusn,SPm1,SPm2,SPm3)
s3 = Student(TPname,TPusn,TPm1,TPm2,TPm3)

print(f"\nAverage of {FPname} with {FPusn} Number is {s1.avg()} marks .")
print(f"Average of {SPname} with {SPusn} is {s2.avg()} marks .")
print(f"Average of {TPname} with {TPusn} is {s3.avg()} marks .\n")

Student.exit_info()
"""
OUTPUT:

******************      BNMIT      ******************

Enter First Person Name: Adarsh Vajpayee
Enter First Person usn: 1BG20IS002
Enter First Person Marks1 : 12
Enter First Person Marks2 : 10
Enter First Person Marks3 : 9

Enter second Person Name: Sunil Kumar
Enter second Person usn: 1BG20IS013
Enter Second Person Marks1 : 28
Enter Second Person Marks2 : 29
Enter Second Person Marks3 : 30

Enter Third Person Name: Prajjwal Chitragar
Enter Third Person usn: 1BG20IS012
Enter Third Person Marks1 : 25
Enter Third Person Marks2 : 23
Enter Third Person Marks3 : 20

Average of Adarsh Vajpayee with 1BG20IS002 Number is 10.333333333333334 marks .
Average of Sunil Kumar with 1BG20IS013 is 29.0 marks .
Average of Prajjwal Chitragar with 1BG20IS012 is 22.666666666666668 marks .

************* Bhaago class khatam hogaya ***************

"""

