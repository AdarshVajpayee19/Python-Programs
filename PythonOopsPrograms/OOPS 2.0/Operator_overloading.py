a = 5
b = 6

# print(a + b)
# print(int.__add__(a, b))  # this is how addition is happening at backside. want to see then click on int. with ctrl

# Magic Methods:
# ex:
# __add__()
# __sub__()
# __mul__()

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)



s1 = Student(58,60)
s2 = Student(62,65)

s3 = s1 + s2
# print(s3.m1) # 118
# print(s3.m2) # 125
print(s1)
print(s2)

if s1 > s2:
    print("s1 is topper")
else:
    print("s2 is topper")


# __add__() here have the same methods but different arguments. may differ in no.of arguments or differ in type.