# 2     5
# 2 3 4 5
s = int(input("enter the start: "))
e = int(input("enter the end: "))
sum = 0
i = s

# s s+1 s+2 ... e
while i <= e:
    sum += i
    i += 1

print(sum)