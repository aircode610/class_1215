nums = []
l = int(input("enter len: "))
for i in range(l):
    a = int(input())
    nums.append(a)

target = int(input("enter target: "))

ans = []
for i in range(l):
    for j in range(l):
        if i == j:
            continue
        if nums[i]+nums[j] == target:
            ans.append((nums[i], nums[j]))
print(ans)
for x,y in ans:
    for m,n in ans:
        if x == n:
            ans.remove((m, n))

for x in ans:
    print(x[0], x[1])