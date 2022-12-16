class A:

    def __init__(self):
        print("In class A constructor")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")


class B:

    def __init__(self):
        print("In class B constructor")

    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")

class C(A,B):
    """
      IMP_NOTE:
            There is conflict arises between (A's or B's) ? super class constructor to be called from Class C constructor,
            since in this program both class A and Class B seperate.
            and C class inherits both A and B.

      We have an concept of MRO (Method Resolution Order)  : it try to execute init of itself first and then goes to left and then right.
      example : Diagram
                        class A Init                class B init
                                  \                    /
                                   \                  /
                                        class C init

                    output: when c class inherits two class A and B. by creating object of c calling c class constructor
                    inside c class constructor calling Super().__init__() constructors.

                          In class A constructor
                          In class C Constructor
                          and then in B constructor.

    """
    def __init__(self):
        super().__init__()
        print("In class C Constructor")

    def feat(self):
        super().feature2()

c1 = C()
c1.feat()
"""

In class A constructor
In class C Constructor
"""

print(C.__doc__)
