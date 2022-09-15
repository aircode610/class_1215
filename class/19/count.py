# 1 : 4
# 2 : 2
# 3 : 3
l = int(input("enter len: "))
nums = []
for i in range(l):
    a = int(input())
    nums.append(a)

count = {}
nums.sort() # [1, 1, 1, 1, 2, 2, 3, 3, 3]

for item in nums:
    if item in count:
        count[item] += 1
    else:
        count.update({item:1})
        # count[item] = 1

for key, value in count.items():
    print(key, ":", value)