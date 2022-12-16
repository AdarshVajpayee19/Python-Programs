# pattern Printing
#
# Input = Integer n
# Boolean = True Or False
#
# True
# *
# * *
# * * *
# * * * *
#
# False
# * * * *
# * * *
# * *
# *

print("Enter The Number Of Rows:")
rows = int(input())
print("Enter '1' Or '0' : ")
num = int(input())
check_if = bool(num)
if check_if == True:
    for i in range(1,rows+1):
        for j in range(1, i+1):
            print("*",end=" ")
        print()
elif check_if == False:
    for i in range(rows,0,-1):
        for j in range(1, i+1):
            print("*",end=" ")
        print()