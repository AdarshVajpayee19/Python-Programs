# Lambda Functions Or Anonymous Functions: One Liner Functions.

minus = lambda x, y: x-y

# def minus(x, y):
#     return x-y

# print(minus(7, -9))

# without using lambda Function

def list_of_lists_first(list_of_lists):
    return list_of_lists[1]

list_of_lists = [[1, 12255],[2, 360],[3, 1720],[4, 1020]]
list_of_lists.sort(key = list_of_lists_first) # sort function takes key as Function which return some index value.
print(list_of_lists)

# use Of Lambda Function

a = [[1, 500],[2, 1000],[3, 120],[4, 1020]]
a.sort(key = lambda x:x[1])
print(a)
