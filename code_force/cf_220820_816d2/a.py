def solution(n,m):
    if n == 1 and m == 1:
        return 0
    mini = min(n,m)
    maxi = max(n,m)
    return maxi + 2 * mini - 2
 
t = int(input())

for _ in range(t):
    N,M = [int(s) for s in input().split()]
    ans = solution(N,M)
    # print("----------------------------", ans)
    print(ans)




# ans1 = solution()
# ans2 = solution()
# print("----------------------------", ans1)
# print("----------------------------", ans2)