# Polymorphism : many forms.-->  that means one thing can take many forms.

# ex : Behave differently at different places.
# ex ; office,college,home

# Four ways of Achieving polymorphism in python.

# 1.Duck Typing.
# 2.Operator Overloading.
# 3.Method Overloading.
# 4.Method Overriding.

# Duck Typing In python

class Pycharm:

    def execute(self):
        print("Compiling...")
        print("Running...")


class Myeditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling...")
        print("Running...")


class Laptop:

    def code(self, ide):
        ide.execute()


print("Enter which editor you want:\n1. to use Pycharm.\n2. to use my editor.\n")
choice = int(input())


match choice:
    case 1:
        ide = Pycharm()
    case 2:
        ide = Myeditor()
    case _:
        ide = Pycharm()
        print("Enter the valid number. otherwise we are using default editor.")

lap1 = Laptop()
lap1.code(ide)
