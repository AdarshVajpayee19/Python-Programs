class Computer:
    def __init__(self, cpu, ram):
        self.ram = ram
        self.cpu = cpu

    def config(self):
        print("Config is ", self.cpu, self.ram)


com1 = Computer('i5', 16) # In the background it is taking 3 arguments ex: Computer(com1,'i5',16),object,value,ram
com2 = Computer('Ry-zen 3', 8)


print(id(com1)) # Gives Address In heap memory
print(id(com2))


com1.config()
com2.config()

