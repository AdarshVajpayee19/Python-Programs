# a = 9
# b = 10
# c = sum((a,b)) # Built In Function
# print(c)

def function1(a, b):
    print("Hello You are In Function1 : ", a + b)
# function1(5, 7)

# Average Between two Numbers.
def func_n2(a, b):
    average = (a + b) / 2
    print("Average of Two Number is = ", average)
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# func_n2(num1, num2)

# Maximum Between Two Numbers.
def func_n3(a, b):
    print(a, " is Greater than ", b) if a > b else print(b, " is Greater than ", a)


# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# func_n3(num1, num2)

# Functions Contain a DocStrings.
# Minimum Between Two Numbers.
def func_n4(a, b):
    """This is the function used to calculate Minimum Between Two Numbers.[This is DocStrings]"""
    return a if a < b else b
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
min_value = func_n4(num1, num2)
print("The minimum between ", num1, " and ", num2, " is : ", min_value)
print(func_n4.__doc__)

