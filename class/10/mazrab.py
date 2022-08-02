m = int(input("from: "))
n = int(input("to: "))

cnt = 0

for i in range(m, n+1):
    if i % 5 == 0:
        print(i, end=" ")
        cnt += 1
print()
print("cnt:", cnt)
