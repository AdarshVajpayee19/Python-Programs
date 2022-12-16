# Lists
# List Datatype.
# list1 = ['python','java','c','html','css']
#
# for items in list1:
#     print(items,end=' ')
#
# list2 = [1, 5, 4, 3, 10,9]
# print("\nAfter appending:")
# list.append(list2,15)
# print(list2)
# print("After sorting:")
# list.sort(list2)
# print(list2)
# print("After Reversing:")
# list.reverse(list2)
# print(list2)
# print("Slicing:")
# print(list2[0:3])
# print(list2[:-1])
#
#
# list3 = [[1, 3, 5],[2,4,6]]
# print(list3)
# print(list3[0])
#
# spam = ['cat','bat','rat','elephant']
# print(spam[0:4])
# print(spam[1:3])
# print(spam[0:-1])
#
# print(spam[:2])
# print(spam[:])
# print(len(spam))
#
#
# # list is a value which is ordered,getting a value from the list using indexes and negative indexes,
# # getting the list from another list with slices.
# # getting the list from len()
# # changing values in a list with indexes.
# spam[0] = 'Prajwal'
# print(spam)
#
# # Concatination and replication.
# list4 = [1 , 2, 3]
# list5 = ['Abhay','Adarsh','Aditi']
# print(list4+list5)
# print(list4*3)
#
# # Delete from list
#
# del spam[0]
# print(spam)
# print(len(spam))
# # Dictionary
#
# dict = {
#     "Money heist":"5 seasons",
#     "Vampire diaries":"8 seasons",
#     "Stranger Things":"4 seasons"
# }
# print(dict)
# print(dict['Vampire diaries'])

# print("enter the name of cat 1:")
# catName1 = input()
# print("enter the name of cat 2:")
# catName2 = input()
# print("enter the name of cat 3:")
# catName3 = input()
# print("enter the name of cat 4:")
# catName4 = input()
# print("enter the name of cat 5:")
# catName5 = input()
# print("enter the name of cat 6:")
# catName6 = input()
# print("The cat names are: ")
# print(catName1+' '+catName2+ ' '+catName3+ " "+catName4+' '+ catName5+' '+catName6+' ')


# catNames = []
# while True:
#     print('Enter the name of cat : '+str(len(catNames)+1)+' or Enter nothing to stop.')
#     name=input()
#     if name =='':
#         break
#     catNames=catNames+[name]
# print('The cat names are: ')
# for name in catNames:
#     print(' '+name)

# Using For loops in lists
# for i in range(4):
#     print(i,end=" ")
#
# print('\n')
# for i in [1, 2,  3, 4]:
#     print(i,end=" ")


# supplies = ['pens', 'staplers', 'flamethrowers', 'binders', 'sunni', 'prajju']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
# supplies.append('Sunil')
# print(supplies)

# Using in and not in operators in list.
# supplies = ['pens', 'staplers', 'flamethrowers', 'binders', 'sunni', 'prajju']
# if 'binders' in supplies:
#     print("Yes")
# else:
#     print("No")

# petnames = ['Rozi','Adu','Ash','Akku','Pragu']
# user_input = input("Enter name:")
# if user_input in petnames:
#     print("Yes name is present in list")
# else:
#     print("No name is not present in list")

# Multiple Assignment trick.
# cat = ['fat','gray','loud']
#
# # 1.Method
# size = cat[0]
# color = cat[1]
# dispositon = cat[2]
# print(size+ ' '+color+ ' '+dispositon)
#
# # 2.method
# size,color,dispositon = cat
# # print(size+ ' '+color+ ' '+dispositon)
# print(f"{size.upper()}, {color.upper()}, {dispositon.upper()}")
#
# supplies = ['pens', 'staplers', 'flamethrowers', 'binders', 'sunni', 'prajju']
# for i,item in enumerate(supplies):
#     print('Index ' + str(i+1) + ' in supplies is: ' + supplies[i].capitalize())


# using a random.choice and random.shuffle functions with list.

# import random
#
# list1 = ['Adarsh', 'sunil', 'prajwal', 'puneeth']
# print(random.choice(list1))
# print(random.choice(list1))
# print(random.choice(list1))
# random.shuffle(list1)
# print(list1)
#
# print(random.randint(1,100))

# Augmented assignment statements (+= , -=, *=, /=, %=).

operation = 'Hello'
operation += ' world'
print(operation)

bacon = ['Sophie']
bacon *= 3
print(bacon)
