def solve(x,y):
    if x == 3 and y == 3:
        return "2 2"
    if x == 2 and y == 3:
        return "1 2"
    if x == 3 and y == 2:
        return "2 1"

    return "1 1"
 
t = int(input())
for _ in range(t):
    x,y = [int(s) for s in input().split()]
    ans = solve(x,y)
    print(ans)