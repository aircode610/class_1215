# 1-2+3-4+5-...-20

sum = 0
sign = 1

# for i in range(1, 101):
#     if i % 2 == 0:
#         sum -= i
#     else:
#         sum += i

for i in range(1, 101):
    sum += i*sign
    sign = -1 * sign

print(sum)

