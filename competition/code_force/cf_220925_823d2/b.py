def solve(n,x,t):
    if n == 1:
        return x[0]
    rP = max(x)
    # when rP is x0
    maxiPos = -1
    maxi = -1
    for i in range(n):
        if maxi < t[i] + rP - x[i]:
            maxi = t[i] + rP - x[i]
            maxiPos = i
    lP = min(x)
    maxiPosL = -1
    maxiL = -1
    for i in range(n):
        if maxiL < t[i] + x[i] - lP:
            maxiL = t[i] + x[i] - lP
            maxiPosL = i
    dis = (- t[maxiPos] + x[maxiPos] + t[maxiPosL] + x[maxiPosL]) / 2
    return dis
 
t = int(input())
for _ in range(t):
    n = int(input())
    x = [int(s) for s in input().split()]
    t = [int(s) for s in input().split()]
    ans = solve(n,x,t)
    # print("----------------------------", ans)
    print(ans)