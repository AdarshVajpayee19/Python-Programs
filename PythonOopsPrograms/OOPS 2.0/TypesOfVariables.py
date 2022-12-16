# TYPES OF VARIABLES:

# 1.Class Variables or Static Variables.
# 2.Static Variables.

# imp_NOTE: Class Variable and Static Variable Are same But Class methods and static methods are different.


class Car:
    wheels = 4  # Class Variable Or static Variables.

    def __init__(self):
        # Instance Variable.
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 6

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

