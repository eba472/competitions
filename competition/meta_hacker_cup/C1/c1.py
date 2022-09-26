
t = int(input())
res = []

def isAllDot(s):
    for char in s:
        if char != ".":
            return False
    return True

def solution(n,c):
    if isAllDot(c):
        ans = []
        for i in range(1,n):
            ans.append("." * len(c) + "-" * i)
        return ans
    ans = []
    for i in range(1,n):
        ans.append("-" * len(c) + "." * i)
    return ans


for i in range(t):
    n = int(input())
    c = input()
    
    res.append(solution(n,c))

with open('output.txt', 'w') as f:
    for i in range(len(res)):
        f.write("Case #{}:\n".format(i+1))
        for code in res[i]:
            f.write(code + "\n")
        
