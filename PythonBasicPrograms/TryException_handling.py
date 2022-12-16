print("Enter Number1 : ")
num1 = input()
print("Enter Number2 : ")
num2 = input()
try:
    print("Sum of Two Numbers: ",
          int(num1)+int(num2))
except Exception as e:
    print(e)
print("This Block of code is important it need to be get Executed!!")
