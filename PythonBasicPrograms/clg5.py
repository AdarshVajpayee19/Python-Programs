# List Methods.

# Finding the value in the list using index() method.


"""


list1 = ['adarsh', 'Prajwal', 'sunil', 'Abhay']
print("Initial List:")
print(list1)
print("Index value is:")
print(list1.index('Prajwal'))
print("After Appending Gopal:")
list1.append('Gopal')
print(list1)
print("After Removing Sunil:")
list1.remove('sunil')
# list1.remove('chicken') error
print(list1)
print("After Reversing:")
list1.reverse()
print(list1)
print("using Insert method:")
list1.insert(1, 'shabri')
print(list1)
print("After Sorting:")
list1.sort(key=str.lower)
print(list1)
print("After Deleting:")
del(list1[2])
print(list1)

spam = "cat"
res = spam.upper()
print(res)
print(res.lower())
#
# n = input("Enter Number of elements you want to insert:")
# list2 = []
# for i,v in enumerate(n):
#     list2[i]=int(input())
# print("Entered values:")
# for i in range(n):
#     print(list2[i],end=" ")
"""


name = 'Zophie'
# print(name[0])
# print(name[-2])
# print(name[0:4])
# print('Zo' in name)
# print('z' in name)
# print('p' not in name)
for i in name:
    print(f'* * * {i} * * *')

