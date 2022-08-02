n = int(input("enter n: "))

mosbat = 0
manfi = 0
sefr = 0

for i in range(n):
    a = int(input())
    if a < 0:
        manfi += 1
    elif a > 0:
        mosbat += 1
    else:
        sefr += 1

print("mosbat:", mosbat)
print("manfi:", manfi)
print("sefr:", sefr)