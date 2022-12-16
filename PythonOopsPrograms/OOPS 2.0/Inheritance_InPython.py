class A:
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")

# Inheritance

class B(A):
    def disp_inherit_text(self):
        print("\nAfter Inheritance i.e. B inherits the Features of A")
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

#Multi level inheritance.

class C(B):
    def disp_inherit_text(self):
        print("\nMultilevel inheritance: c inherits both class A and B features.")

    def feature5(self):
        print("Feature 5 working")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.disp_inherit_text()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1 = C()
c1.disp_inherit_text()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()


