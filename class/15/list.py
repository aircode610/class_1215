#creating
category = ["electronics", "home", "kids"]
print(category)

print()

#length
print(len(category))

print()

#multiple type
list1 = [23, True, "salam"]
print(list1)

print()

#type
print(type(list1))

print()

#casting
l = list((2, 3, 7))
print(l)

print()

#accessing list items
print(list1[0])
print(list1[-1])
print(list1[:2])

print()

#in
if 23 in list1:
    print("yes")

print()

#changing one item
list1[1] = False
print(list1)

print()

#change range
list1[:2] = [43, 96]
print(list1)

print()

#insert
list1.insert(2, "khodafez")
print(list1)

print()

#append
list1.append(72)
print(list1)

print()

#extend
a = [3, 5, 7]
list1.extend(a)
print(list1)

print()

#remove
list1.remove("salam")
print(list1)

print()

#pop
list1.pop(2)
print(list1)
list1.pop()
print(list1)

print()

#del
del list1[0]
print(list1)
del list1
#print(list1)

print()

#clear
category = []
print(category)
list2 = [1, 2, 3]
list2.clear()
print(list2)

print()

#sort
unsorted = [5, 2, 7, 4, 9]
unsorted.sort(reverse=True)
print(unsorted)

#reverse
unsorted.reverse()

print()

#unlink(copy)
list3 = unsorted.copy()
# list3 = list(unsorted)
unsorted.append(10)
print(list3)

print()

#join
joined = list3+unsorted
print(joined)

print()

#count
print(joined.count(2))