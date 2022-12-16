def function1():
    print("Subscribe Now")

func2 = function1
del function1
# func2()
# OUTPUT:Subscribe Now
#
# def funret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
#     if num == 2:
#         return sum
#
# a = funret(0)
# print(a)

# def executer(func):
#     func("this ")
#
# executer(print)


def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_adarsh():
    print("Adarsh is a good boy")

# who_is_adarsh = dec1(who_is_adarsh) # else @dec1
who_is_adarsh()

# Executing now
# Adarsh is a good boy
# Executed


