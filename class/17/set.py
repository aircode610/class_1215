#define
s = {1, 3, 7}

#add
s.add(9)
print(s)

print()

#update
s2 = {5, 9}
s.update(s2)
print(s)

print()

#remove
s.remove(9)
print(s)

print()

#discard
s.discard(9)
print(s)

print()

#pop
s.pop()
print(s)

print()

#clear
s.clear()
print(s)

#del
del s
# print(s)

print()

#union
a = {1, 2, 5, 7}
b = {1, 4, 10, 5}

c = a.union(b)
# a.update(b)
print(c)

print()

#intersection
c = a.intersection(b)
# a.intersection_update(b)
print(c)

print()

#symmetric difference
c = a.symmetric_difference(b)
# a.symmetric_difference_update(b)
print(c)

print()

#subset
c = {4, 5}
sub = c.issubset(b)
print(sub)

print()

#superset
sup = b.issuperset(c)
print(sup)

print()

#disjoint
dis = a.isdisjoint(b)
print(dis)

print()

#difference
print(a-b)
print(a.difference(b))

print()