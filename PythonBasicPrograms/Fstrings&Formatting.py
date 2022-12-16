# Fstrings And formatting

import math
# Formatting
me = "Adarsh Vajpayee"
a1 = 3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# a = "This is {} {}"
# b = a.format(me, a1)
# print(b)

# Fstrings : Fast Strings
c = f"this is {me} {a1} {69} {math.sin(45)}"
print(c)


