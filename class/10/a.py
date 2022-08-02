# alireza => 2
str = input("enter a string: ")
cnt = 0

for i in range(len(str)):
    if str[i] == 'a':
        cnt += 1

print(cnt)