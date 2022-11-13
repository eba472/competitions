n = int(input())
s = []

for i in range(n):
    s.append(input())


def sol(s):
    for i in range(len(s)):
        if s[i][0] not in "HDCS":
            return "No"
        if s[i][1] not in "A23456789TJQK":
            return "No"
        for j in range(i+1, len(s)):
            if s[j] == s[i]:
                return "No"
    return "Yes"


print(sol(s))
