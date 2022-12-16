grocery = ["Harpic", "Vim Bar", "Bhindi", "LollyPop"]

print(grocery)
print(grocery[1])
print(grocery[2:])
print(grocery[1]+" "+grocery[3])

numbers = [2,  4, 117, 19, 10]
print(numbers)  # Printing List
numbers.sort()  # It will Change the original list
print(numbers)  # After Sort
numbers.reverse()   # it will change the original list
print(numbers)  # After Sort And Reverse
print(numbers[2])
print(numbers[1])
print(numbers[1:4])
print(numbers[::2])  # skipping one value

# In negative slicing it is better to take -1 not less than then this like -3,-2-4 etc......
number = [2, 4, 5, 7, 3, 5, 5, 4, 10, -1]
print("The length of the list = "+str(len(number)))
print("The Maximum in the list is = "+str(max(number)))
print("The Minimum in the list is = "+str(min(number)))
print("The sum is = "+str(sum(number)))
number.append(15)
print(number)
number.insert(2, 67)
print(number)
number.remove(67)
print(number)
number.pop()
print(number)

number[1] = 100
print(number)

# Mutable : Can change. EX : LIST
# Immuatable : cannot Change. EX : TUPLE

# tuple: immutable
tp = {1, 2, 3}
print(tp)

# Swapping
a = 1
b = 8
print("The value Of a before Swap is : "+str(a))
print("The value Of b before Swap is : "+str(b))
"""
1. One method (Traditional way to swap)

temp = a
a = b
b = temp

2.By using Python cool feature 
"""
a, b = b, a
print("The new value Of a After Swap is : "+str(a))
print("The new value Of b After Swap is : "+str(b))
