class computer:

    def config(self):
        print("i5,\t16gb,\t1tb")

# x = 9
# print(type(x))

# a = '8'
# print(type(a))

com1 = computer()
com2 = computer()
# print(type(com1))

computer.config(com1)
computer.config(com2)

# or

com1.config()
com2.config()
