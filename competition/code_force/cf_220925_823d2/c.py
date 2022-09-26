def solve(x):
    behMini = 10
    for i in range(len(x)-1, -1,-1):
        if x[i] > behMini:
            x[i] = min(x[i]+1, 9)
        else:
            behMini = x[i]
    return "".join([str(i) for i in sorted(x)])
    
t = int(input())
for _ in range(t):
    x = [int(s) for s in list(input())]
    ans = solve(x)
    # print("----------------------------", ans)
    print(ans)