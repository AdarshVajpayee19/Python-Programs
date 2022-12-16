# i = 0
# while True:
#     if i+1 < 5:
#         i = i + 1
#         continue
#     print(i+1, end=" ")
#     if i == 44:
#         break # Stop the loop
#     i = i + 1

print("Enter number greater than 100 To Terminate The Program.\n")
while True:
    inp = int(input("Enter a number '<' 100 : \n"))
    if inp > 100:
        print("You have Entered, The Value Greater than 100 Exit the Program\n")
        break
    else:
        print("Try Again!\n")
        continue
