
# No need to write this code use below code one 'with open()'.
# f = open("Adarsh.txt","rt")
# f.close()

# No need close file when you are reading from file.
with open("Adarsh.txt") as f:
    a = f.read(4)
    print(a)
