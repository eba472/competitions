def solve(n,c,a):
    orbit = {}
    for i in a:
        orbit[i] = orbit.get(i,0) + 1
    cost = 0
    for o in orbit:
        cost += min(orbit[o], c)
    return cost
 
t = int(input())
for _ in range(t):
    n,c = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    ans = solve(n,c,a)
    # print("----------------------------", ans)
    print(ans)



