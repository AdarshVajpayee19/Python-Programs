# f = open("WriteMode.txt","w")
# f.write("Adarsh Ko naye naye chees sichna pasnad hai.\n")
# f.close()

# f = open("AppendMode.txt", "a")
# a = f.write("Adarsh Ko naye naye chees sichna pasnad hai.\n")
# print(a)
# f.close()

# Handle Read And Write Both
f = open("sample.txt", "r+")
print(f.read())
f.write("Thank You")
