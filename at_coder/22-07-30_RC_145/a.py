n = int(input())
s = input()

if n == 2:
    if s[0] == s[1]:
        print("Yes")
    else:
        print("No")
else:
    if s[0] == "A" and s[-1] == "B":
        print("No")
    else:
        print("Yes")