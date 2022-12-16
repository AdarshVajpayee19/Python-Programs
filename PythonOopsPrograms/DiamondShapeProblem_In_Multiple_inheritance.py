class A:
    def met(self):
        print("This is a Method From class A.")

class B(A):
    def met(self):
        print("This is a Method From class B.")

class C(A):
    def met(self):
        print("This is a Method From class C.")

class D(B, C):
    def met(self):
        print("This is a Method From class D.")

a = A()
b = B()
c = C()
d = D()

c.met()