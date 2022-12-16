f = open("Adarsh.txt")
# print(f.tell()) # gives the position of the file pointer.
print(f.readline())
# print(f.tell())
f.seek(0) # It is reseting the file pointer postion back to 0.
print(f.readline())
# print(f.tell())
f.close()
