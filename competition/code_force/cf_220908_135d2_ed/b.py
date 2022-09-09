def solution(n):
    if n == 1:
        return "1"
    if n == 2:
        return "1 2"
    if n == 3:
        return "2 1 3"
    
    if n % 2 == 0:
        return " ".join([str(i) for i in range(n-2, 0,-1)]) + " " + str(n-1) + " " + str(n)
    else:
        return "1 " + " ".join([str(i) for i in range(n-2, 1,-1)]) + " " + str(n-1) + " " + str(n)

    return 
 
t = int(input())

for _ in range(t):
    n = int(input())
    ans = solution(n)
    # print("----------------------------", ans)
    print(ans)
