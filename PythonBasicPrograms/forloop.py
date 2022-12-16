# List
# list1 = ["Adarsh", "Gnanesh", "Manoj", "Gopal", "Shabri"]

# Tuple
# list1 = ("Adarsh", "Gnanesh", "Manoj", "Gopal", "Shabri")

# List of Lists
list1 = [["Adarsh", 10], ["Gnanesh", 7], ["Manoj", 15], ["Gopal", 12], ["Shabri", 20]]

# for item, lollypop in list1:
#     print(item,"Eats", lollypop)

# After Typecasting List to Dictionary
dict1 = dict(list1)
print(dict1)
print("if We want only Keys and Value Both then use (for item, lollypop in dict1.items():) :")
for item, lollypop in dict1.items():
    print(item, "Eats", lollypop)

print("if We want only Keys then use (for item in dict1:) :")
for item in dict1:
    print(item)

items_list = [int, float, "Adarsh", 5, 3, 4, 6, 7, 10, 200, 500, 2000]

for item in items_list:
    if str(item).isnumeric() and item > 5:
        print(item)
