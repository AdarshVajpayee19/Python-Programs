class A:

    def __init__(self):
        print("In class A constructor")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")


class B(A):
    """
    Imp_Note:
        if you create object of subclass it will try to find init of subclass,
        if it is not found then it will call init of super class.
        say now we want access constructor of Super class or some methods we can do so by using super keyword.
    """

    def __init__(self):
        super().__init__()
        print("In class B constructor")

    # When there is no constructor in class B it goes to A constructor. output is  In class A constructor
    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")


b1 = B()

var = B.__doc__
print(var)
