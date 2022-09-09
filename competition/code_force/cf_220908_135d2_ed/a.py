def solution(n,a):
    m = max(a)
    s = sum(a)
    return a.index(m) + 1
 
t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    ans = solution(n,a)
    # print("----------------------------", ans)
    print(ans)
