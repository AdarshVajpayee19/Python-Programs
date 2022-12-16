f1 = open("adarsh.txt")

try:
    f = open("does.txt")
except EOFError as e:
    print("EOF error aa gaya",e)
except IOError as e:
    print("IO error aa gaya",e)
# Except aur Else mein se sirf ek cheez run karti hai.
else:
    print("This will run only if except is not running...")

# ye kaam toh karna hi karna hai
finally:
    print("Run this anyway...")
    f1.close()
print("Important Stuff")

