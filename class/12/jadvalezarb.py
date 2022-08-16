n = int(input("enter n: "))

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(i*j, end=" ")
#     print()

for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        sum += i
        print(sum, end=" ")
    print()

#   1 2 3 4
# 1 1 2 3 4
# 2 2 4 6 8
# 3 3 6 9 12
# 4 4 8 12 16