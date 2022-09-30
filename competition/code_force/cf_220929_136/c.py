def solve(x):
    if x == 2:
        return [1,0,1]
    ini = [1,0,1,2]
    mod = 998244353 
    for i in range(4,x+2,2):
        nex = [0,0,1,0]
        nex[3] = ini[3] * i * (i-1) // (i//2) // (i//2)
        nex[0] = nex[3] // 2 + ini[1]
        nex[1] = nex[3] - nex[0] - 1
        ini = nex
    return [i % mod for i in ini[:3]]
    
t = int(input())
for _ in range(t):
    x = int(input())
    ans = solve(x)
    # print("----------------------------", ans)
    print(" ".join([str(i) for i in ans]))