#define
car = {
    "brand" : "benz",
    "model" : "s600",
    "year" : 2022
}

#len
print(len(car))

print()

#type
print(type(car))

print()

#access
print(car["year"])
print(car.get("year"))

print()

#keys
keys = car.keys()
print(keys)

print()

#values
values = car.values()
print(values)

print()

#items
items = car.items()
print(items)

print()

#exist key
if "model" in car:
    print("yes")

print()

#change
car["model"] = "s500"
print(car)

print()

#update
car.update({"model":"s600", "cylinder":12})
print(car)

print()

#pop
car.pop("brand")
car.popitem()
print(car)

print()

#delete
del car["model"]
# del car
print(car)

print()

#clear
car.clear()
print(car)

print()

#copy
car2 = car.copy()

#nested dict
cars = {
    "car1": {
        "brand" : "benz",
        "model" : "s600"
    },
    "car2" : {
        "brand" : "ford",
        "model" : "mustang"
    }
}

print(cars["car2"]["model"])