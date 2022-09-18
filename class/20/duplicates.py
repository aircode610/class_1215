tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)

# dup = []
# for x in tup:
#     if x not in dup:
#         dup.append(x)
# print(tuple(dup))

print(tuple(set(tup)))