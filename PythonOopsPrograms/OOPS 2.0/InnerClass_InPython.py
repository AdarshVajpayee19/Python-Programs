# Imp_NoTE: You can create object of Inner class inside the outer class or
# You can create the object of inner class Outside the outer class provided you use outer class name to call it.

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(f"Name: {self.name} and RollNo: {self.rollno}.")
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = 4

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Adarsh',2)
s2 = Student('prajwal',12)

s1.show()
s2.show()

# print(s1.lap.brand)

# or
# lap1 = s1.lap
# lap2 = s2.lap




# print(id(lap1))
# print(id(lap2))

# Creating Laptop class outside
lap1 = Student.Laptop()
lap2 = Student.Laptop()

