# a = int(input())
# b = int(input())
# c = int(input())

mx = 0

# if a > max:
#     mx = a
# if b > max:
#     mx = b
# if c > max:
#     mx = c

n = int(input("enter n: "))

for i in range(n):
    a = int(input())
    # if a > max:
    #     mx = a
    mx = max(mx, a)

print(mx)