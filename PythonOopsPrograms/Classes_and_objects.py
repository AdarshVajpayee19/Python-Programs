# Classes - Template
# Object - Instance of the class

# Works on the concept of DRY - Do not Repeat Yourself.
class Student:
    pass

adarsh = Student()
gnanesh = Student()

adarsh.name = "Adarsh Vajpayee"
adarsh.std = "3"
adarsh.section = "B"

gnanesh.name = "Gnanesh Auti"
gnanesh.std = "4"
gnanesh.section = "A"

print(adarsh, gnanesh)
print("Adarsh Details : ")
print(adarsh.name)
print(adarsh.section)
print(adarsh.std)

print("\n")
print("Gnanesh Details : ")
print(gnanesh.name)
print(gnanesh.section)
print(gnanesh.std)


