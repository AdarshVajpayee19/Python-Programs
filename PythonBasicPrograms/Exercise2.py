# Exercise 2 : Faulty Calculator
# 45*3=555,   56+9=77,       56/6=4

# Design a calculator which will correctly solve all the problems except the following ones:
# 45*3=555,   56+9=77,       56/6=4
# Your Program should take operator and the two numbers as input from the user and then return the result.

print("Enter Operator (+, -, *, %, /) : ")
operator = input()
print("Enter First Number : ")
num1 = int(input())
print("Enter Second Number : ")
num2 = int(input())

if operator == '+':
    if num1 == 56 and num2 == 9:
        print("77")
    else:
        print(num1+num2)
elif operator == '/':
    if num1 == 56 and num2 == 6:
        print("4")
    else:
        print(num1/num2)
elif operator == '*':
    if num1 == 45 and num2 == 3:
        print("555")
    else:
        print(num1*num2)
elif operator == '-':
    print(num1-num2)
elif operator == '%':
    print(num1%num2)
else:
    print("Plz Enter the Valid Operator")
