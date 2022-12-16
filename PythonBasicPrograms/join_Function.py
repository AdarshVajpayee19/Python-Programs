list = ["John","Cena","Randy","Ortan","Sheamus","Khali","Jinder","mahal"]


# Required Output: John and Cena and Randy and Ortan and Sheamus and Khali and Jinder and mahal Other WWE Superstars....
# for item in list:
#     print(item,"and ",end="")

# instead do this
a = " and ".join(list)

print(a," Other WWE Superstars....")
