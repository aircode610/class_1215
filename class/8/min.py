mn = 1000
n = int(input("enter n: "))

for i in range(n):
    a = int(input())
    # mn = min(a, mn)
    if a < mn:
        mn = a

print(mn)