def factorial_iterative(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact

def factorial_recursive(n):
    if n == 0 or n == 1:
        return  1
    else:
        return n*factorial_recursive(n-1)

num = int(input("Enter Factorial and nth Fibonacci Of number you want: "))
print("Factorial Of Number using Recursive Appraoch : ", factorial_recursive(num))
print("Factorial Of Number Using Iterative Appraoch : ", factorial_iterative(num))

# Nth-Fibonacci Number

def nth_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fibonacci(n-1)+nth_fibonacci(n-2)

# num = int(input("Enter the nth fibonacci Number You Want:"))
print("The Nth Fibonacci Number Is : ", nth_fibonacci(num))
