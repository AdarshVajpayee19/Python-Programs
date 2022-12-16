# ***********************************************************   MAP   **************************************************************

numbers = ["3","34","64"]

# Everytime running a for loop is not good
# for i in range(len(numbers)):
#     numbers[2] = int(numbers[2])

# instead do this
# use map Function
# map function performs int() to all elements in numbers list, and after that typecasting that into list.

numbers = list(map(int,numbers))
#
# numbers[2] = numbers[2] + 1
# print(numbers[2])

num = [2, 3, 4, 5, 7, 6, 9, 10]

# def sq(x):
#     return x*x

# square = list(map(lambda x:x*x,num))
# print(square)

cube_num = ["1","3","5","7","9"]

# By Adarsh Vajpayee
# cube = list(map(lambda x:x*x*x,map(int,cube_num)))
# print(cube)

def sq2(a):
    return a*a

def cu3(a):
    return a*a*a

funcn = [sq2, cu3]

for i in range(11):
    val = list(map(lambda x:x(i), funcn))
    # print(val)



# *******************************************************     FILTER     **************************************************************

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_greater_than_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_than_5,list_1))
# print(gr_than_5)

# *******************************************************     REDUCE     **************************************************************

from functools import reduce

list1 = [1, 2, 3, 4]

# num = 0
# for i in list1:
#     num = num + i
#
# print(num)

# instead do this

num = reduce(lambda x,y:x+y,list1)
mul =  reduce(lambda x,y:x*y,list1)
sub =  reduce(lambda x,y:x-y,list1)

print(num)
print(mul)
print(sub)

