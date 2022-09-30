def solve(n,a):
    res = [a[0]]
    for i in range(1,n):
        if a[i] == 0:
            res.append(res[-1])
        else:
            x1 = a[i] + res[i-1]
            x2 = res[i-1] - a[i]
            if (0 <= x1) and (0 <= x2):
                return [-1]
            if 0 <= x1:
                res.append(x1)
            if 0 <= x2:
                res.append(x2)
    return res
 
t = int(input())
for _ in range(t):
    n = int(input())
    x = [int(s) for s in input().split()]
    ans = solve(n,x)
    # print("----------------------------", ans)
    print(" ".join([str(i) for i in ans]))