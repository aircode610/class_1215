str = input("enter a string: ")
rev = ""

for i in range(len(str)-1, -1, -1):
    rev += str[i]

if rev == str:
    print("symmetrical")
else:
    print("not symmetrical")