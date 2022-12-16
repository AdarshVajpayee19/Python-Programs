# print("Using For loop")
# for i in range(5):
#     print('Adarsh five times ('+str(i)+')')
# print("\nUsing While loop")
#
# i=0
# while i < 5:
#     print('prajwal five times ('+str(i)+')')
#     i = i + 1


# write a program to add all numbers from zero to hundred
# sum = 01


# for i in range(0,10,2):
# for i in range(12,13):
#
# for i in range(101):
#     print(i)
#     sum = sum + i
# print("The sum of hundred numbers is (1-100): ",sum)
#
# for i in range(5,-1,-1):
#     print(i)

# import random
#
# # r_num = random.randint(1,100)
# # print(r_num)
# list = [1, 3, 6, 10, 18]
# for i in range(5):
#     # print(random.randint(1,10))
#     print(random.choice(list),end=" ")
#
# import sys
#
# while True:
#     print('\nType exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed '+response+'.')

# program 9
# spam = int(input("Enter number :"))
# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print('Howdy')
# else:
#     print('Greetings!')

# program 13
# print("using for loop")
# for i in range(11):
#     if i == 0:
#         continue
#     print(i)
#
# print("\nUsing while loop")
# i=1
# while i<11:
#     print(i)
#     i = i+1
#
# def becon(str):
#     print(f"Hello, i am {str}")
# becon("Adarsh")
#
# def hello():
#     print('Hello')
#     print('Hi')
#     print('Bye')
#
# hello()
# hello()
# hello()

# Functions

# A function is like a mini program with in a progam
# Parameters are variables that contains argument
# when a function is called with argument the arguments are stored in parameters
# a value being pass to function in a function call is an agrument.
# variables that have arguments assigned to them are parameters


# Return values and Return statements:

# import random
#
#
# def get_ans(num):
#     if num == 1:
#         return 'Answer 1'
#     elif num == 2:
#         return 'Answer 2'
#     elif num == 3:
#         return 'Answer 3'
#     elif num == 4:
#         return 'Answer 4'
#     elif num == 5:
#         return 'Answer 5'
#     elif num == 6:
#         return 'Answer 6'
#     elif num == 7:
#         return 'Answer 7'
#     elif num == 8:
#         return 'Answer 8'
#
#
# print(get_ans(random.randint(1, 8)))
#
#
# def fact(number):
#     if number == 0:
#         return 1
#     elif number == 1:
#         return 1
#     else:
#         return number * fact(number - 1)
#
#
# print(fact(random.randint(1, 10)))
#
# print('cats', 'dogs', 'mice')
# print('cats', 'dogs', 'mice', sep=",")


# str = 'cats-dog-mice'
# def string_split(str):
#     return string_split.split("-")

# print(string_split(str))

# def spam(divideby):
#     return 42 / divideby
#
#
# print(spam(12))
# print(spam(1))
#
# # Handling Exception
# try:
#     print(spam(0))
# except Exception as e:
#     print(e, "Invalid Argument...")
#
# print(spam(13))

# parameters are variables that are assigned in a called function are said to be existed in local scope. variables that
# are assigned outside all functions are set to exists in global scope a variable that exists in local scope is
# called a local variable. a variable that exist in global scope is called global variable. A variable must be one
# are the other it cannot be both local and global. a local Scope is created whenever a function is called. any
# variables assigned in the function exists with the function local scope. When the function return the local scope is
# destroyed and these variables are forgotten. the next time u called the function the local variables will not
# remember the value stored in them from the last time function got called.

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)
#
# def bacon():
#     ham = 101
#     eggs = 0
# spam()
# print(eggs)

#
# def spam():
#     print(eggs)
#
#
# eggs = 42
# spam()
#
#
# def spam1():
#     eggs = 'hello'
#     print(eggs)
#
#
# eggs = 42
# spam1()
# print(eggs)

# def spam():
#     eggs = 'spam local'
#     print(eggs)
#
# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
#     spam()
#     print(eggs)
#
# eggs = 'global'
# bacon()
# print(eggs)

# def sq(n):
#     return n*n
# num = int(input("Enter the number: "))
# re = sq(num)
# print(re)

def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'
spam()
print(eggs)

