# File Io Basics
"""
"r" -> Open file for reading. --> Default mode
"w" -> Open a file for writing.
"x" -> Creates File if not exists.
"a" -> Add more Content to a file.
"t" -> text mode. --> Default
"b" -> binary mode.
"+" -> read and write
"""
# f = open("Adarsh.txt","rt")
#
# # content = f.read(6)
# # print(content)
# # content = f.read(10)
# # print(content)
#
# content = f.read()
# print(content)
# f.close()

f = open("Adarsh.txt")
# for line in f:
#     print(line,end="")

# print(f.readline())
# print(f.readline())

print(f.readlines())
f.close()
