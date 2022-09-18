k = int(input("divisor: "))
nums = [(4, 6, 7), (3, 6, 10, 11), (4, 12, 16)]

# nums = []
# n = int(input("enter list len: "))
# for i in range(n):
#     t = []
#     nt = int(input("enter tuple len: "))
#     for j in range(nt):
#         a = int(input())
#         t.append(a)
#     nums.append(tuple(t))

for tup in nums:
    div = True
    for item in tup:
        if item % k != 0:
            div = False
    if div == True:
        print(tup)