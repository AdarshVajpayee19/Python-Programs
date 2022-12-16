class Employee:
    no_of_leaves = 8
    var = 500
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_no_of_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is Good ",string)

class player:
    no_of_games = 4
    var = 750
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The name is {self.name} and game is {self.game}"

adarsh = Employee("Adarsh vajpayee",30_000,"FrontEnd Developer")
manoj = Employee("Manoj Gouda",25_000,"Business administrator")

bhupal = player("Bhupal Ram", ["cricket"])
rajat = player("Rajat Yadav",["Basket ball"])

# Here Order is important First Employee is created and Second Player
class CoolProgrammer(Employee, player):
    var = 1000
    language = 'C++'
    def printlanguage(self):
        print(self.language)

gnanesh = CoolProgrammer("Gnanesh Auti",60_000,"Junior CA")
print(gnanesh.printdetails())
print(gnanesh.var)

# if same variable is present in Coolprogrammer,Employee,Player it will take first Coolprogrammer and then Employee and then player.

