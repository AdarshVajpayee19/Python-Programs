# Dictionary is nothing but Key Value Pairs
d1 = {}
print(type(d1))

d2 = {"Adarsh": "Veg Roll", "Gnanesh": "Mysore Bonda",
      "Manoj Gowda": "Chicken pullow", "Gopal": {"B": "Maggie", "L": "Rice Dal", "D": "Daaru"}}

print(d2)

print(d2["Adarsh"])
print(d2["Gnanesh"])
print(d2["Manoj Gowda"])
print(d2["Gopal"])
print(d2["Gopal"]["D"])

d2["Shabri"] = "Junk Food"
print(d2)
del(d2["Shabri"])
print(d2)

d3 = d2
del(d3["Adarsh"])
print(d2)   # though it deleted from d2, when u do d3 = d2 ,both are pointers pointing to the same dictionary.

d3 = d2.copy()
del(d3["Gopal"])
print(d2)   # when u do d3 = d2.copy() it will avoid the above problem it will delete from copied dictionary hence no problem in previous dictionary.

d2.update({"Akshita": "Toffee"})
print(d2)
d2.update({"Adarsh Vajpayee": "Chutney"})
print(d2)

print(d2.keys())
print(d2.items())

