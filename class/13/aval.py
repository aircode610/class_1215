# 12
# 2 3 4 5 6 7 8 9 10 11
# 5: 2 3 4
a = int(input("enter: "))
aval = True

for i in range(2, a):
    if a % i == 0:
        aval = False

if aval:
    print("aval")
else:
    print("morakab")

