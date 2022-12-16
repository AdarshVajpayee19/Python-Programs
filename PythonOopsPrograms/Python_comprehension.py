# list = []
#
# for i in range(100):
#     if i%3 == 0:
#         list.append(i)
#
# print(list)

# same above thing in one line.


# List Comprehension.
print("List Comprehension:")
list1 = [i for i in range(100) if i%3 == 0]
print(list1)
print(type(list1))
print('\n')

# Dictionary Comprehension.
print("Dictionary Comprehension:")
dict1 = {i:f"item{i}" for i in range(1, 100) if i%2==0}
print(dict1)
print(type(dict1))
print('\n')

# reversing dic
print("Reversing key and value converse of above Dictionary comprehension: ")
dict2 = {i:f"item{i}" for i in range(100)}
dict2 = {value:key for key,value in dict1.items()}
print(dict2)
print(type(dict2))
print('\n')


# Set Comprehension.
print("Set Comprehension: ")
dresses = {dress for dress in ["dress1","dress2",
                               "dress1","dress2",
                               "dress1","dress2"]}
print(type(dresses))
print(dresses)
print('\n')

dresses1 = [dress for dress in ["dress1","dress2",
                               "dress1","dress2",
                               "dress1","dress2"]]
print(type(dresses1))
print(dresses1)
print('\n')

# Generator Comprehension.
print("Generator Comprehension: ")
evens = (i for i in range(100) if i%2  == 0)
print(type(evens))
print(evens)
# print(evens.__next__())

# to print all
for i in evens:
    print(i,end=" ")

print('\n')

