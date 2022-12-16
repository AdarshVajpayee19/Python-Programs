import json

data = '{"var1":"adarsh", "var2":56}'

parsed = json.loads(data)
print(parsed)
print(type(parsed))
print(parsed['var1'])

data2 = {
    "channel name": "Coding journey",
    "cars":['bmw', 'audi a8', 'ferrai'],
    "fridge":('roti',549)
}

jscomp = json.dumps(data2)
print(jscomp)

