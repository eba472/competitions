
t = int(input())
res = []

def isThereTree(r,c,p):
    for i in range(r):
        for j in range(c):
            if p[i][j] == "^":
                return True
    return False

def solution(r,c,p):
    if not isThereTree(r,c,p):
        return [True, p]
    
    if r == 1 or c == 1:
        return [False, '']
    
    for i in range(r):
        p[i] = "^" * c 
    return [True, p]

for i in range(t):
    r, c = [int(i) for i in input().split()]
    p = []
    for _ in range(r):
        p.append(input())
    
    res.append(solution(r,c,p))
print(res)

with open('validation_output.txt', 'w') as f:
    for i in range(len(res)):
        ok, painting = res[i]
        if ok:
            f.write("Case #{}: Possible\n".format(i+1))
            for r in painting:
                f.write(r + "\n")
        else:
            f.write("Case #{}: Impossible\n".format(i+1))
