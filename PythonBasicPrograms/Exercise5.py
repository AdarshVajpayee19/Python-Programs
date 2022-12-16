# Health Management System
# 3 - clients --> Harry, Rohan and Hammad
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()

# Total  6 files
# Write a function that when executed takes an input client_name
# []timestamp chicken Roti
# One more function to retrieve exercise or food for any client

print("**************** HEALTH MANAGEMENT SYSTEM *****************")

# By Adarsh Vajpayee

# def get_client_name():
#     cilent_name = input("Enter Cilent name : ")
#     return cilent_name
#
# def get_Exercise_or_food():
#     e_or_f = input("Enter Exercise or Food Details You want: ")
#     return e_or_f
#
# def retrieve_exer_or_food():
#     member = get_client_name()
#     # print("Gym Member Name is: ", member)
#     if member == 'Harry':
#         choice = get_Exercise_or_food()
#         # print("Enter Exercise or Food Details You want of the ",member," :", choice)
#         if choice == 'Exercise':
#             f = open("HarryExercise.txt")
#             h = f.read()
#             print("[ ", getdate(),"]", h)
#             f.close()
#         elif choice == 'Food':
#             f = open("HarryFood.txt")
#             h = f.read()
#             print("[ ", getdate(),"]", h)
#             f.close()
#         else:
#             print("Enter Valid Choice Please !!!")
#     elif member == 'Rohan':
#         choice = get_Exercise_or_food()
#         # print("Enter Exercise or Food Details You want of the ", member, " :", choice)
#         if choice == 'Exercise':
#             f = open("RohanExercise.txt")
#             h = f.read()
#             print("[", getdate(),"]", h)
#             f.close()
#         elif choice == 'Food':
#             f = open("RohanFood.txt")
#             h = f.read()
#             print("[ ", getdate(),"]", h)
#             f.close()
#         else:
#             print("Enter Valid Choice Please !!!")
#     elif member == 'Hammad':
#         choice = get_Exercise_or_food()
#         # print("Enter Exercise or Food Details You want of the ", member, " :", choice)
#         if choice == 'Exercise':
#             f = open("HammadExercise.txt")
#             h = f.read()
#             print("[ ", getdate(),"]", h)
#             f.close()
#         elif choice == 'Food':
#             f = open("HammadFood.txt")
#             h = f.read()
#             print("[ ", getdate(),"]", h)
#             f.close()
#         else:
#             print("Enter Valid Choice Please !!!")
#     else:
#         print("Enter a Valid Name!!! ")
#
# retrieve_exer_or_food()

# Health Management System
# 3 clients - Harry, Rohan and Hammad

import datetime

def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("HarryExercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("HarryFood.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("RohanExercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("RohanFood.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("HammadExercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("HammadFood.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad))")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("HarryExercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("HarryFood.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("RohanExercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("RohanFood.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("HammadExercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("HammadFood.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")

a = int(input("Press 1 for log the value and 2 for retrieve : "))

if a == 1:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad : "))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad :  "))
    retrieve(b)

