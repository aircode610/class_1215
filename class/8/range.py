# n = 5
# 2 5 1 7 2 (adad az 1 ta 100)
# max
# min

mx = 0
mn = 101

n = int(input("enter n: "))
for i in range(n):
    a = int(input())
    mx = max(mx, a)
    mn = min(mn, a)

print("range:", mn, "-", mx)