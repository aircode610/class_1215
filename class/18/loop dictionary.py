car = {
    "brand" : "benz",
    "model" : "s600",
    "year" : 2022
}

#loop dict
for x in car:
    print(x) #keys
    print(car[x]) #values

print()

#loop keys
for x in car.keys():
    print(x)

print()

#loop values
for x in car.values():
    print(x)

print()

#loop items
for x,y in car.items():
    print(x, y)