# Method Overloading is Not supported in python. i.e we can write a method with the same name.

# But we're trying to achieve method overloading by varies ways.
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s =a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a

        return s

s1 = Student(58,60)

print(s1.sum(56,44))
print(s1.sum(56,44,100))
print(s1.sum(56))


