"""
Iterable - __iter__() or __getitem__()  provides if the object is iterable or not. if object is iterable then it generates iterator.
Iterator - __next__()
Iteration -

Generators are the type of iterators which we can able to iterate once.
for ex: range is iterator, yield

apna generate kaise bante hai lets see.
"""

def gen(n):
    for i in range(n):
        yield i


g = gen(3) # ur generator is cable of generating between 0 to 2.
print(g)
# <generator object gen at 0x0000027E2E0404A0>
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())

for i in g:
    print(i)
# for loop are designed in such a way that when iterator ends it will not leads to error ,for loop will Handle.


# string is iterable so we can iterate it.
a = "Adarsh"

# <generator object gen at 0x0000027E2E0404A0>
# a = 4354542

for c in a:
    print(c)

n = 45424524
ier = iter(n)

print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
