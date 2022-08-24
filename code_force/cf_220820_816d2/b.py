def solution(n, k, b, s):
    if s < k * b or s > b*k + n * (k-1):
        return -1
    if k == 1:
        ans = [0] * (n-1)
        ans.append(s)
    else:
        ans = [0] * n
        ans[0] += k*b
        remove = s - k * b
        left = remove % (k - 1)
        howMany = remove // (k - 1)

        for i in range(howMany):
            ans[i] += k-1
        if left != 0:
            ans[howMany] += left
    return " ".join([str(i) for i in ans])


t = int(input())

for _ in range(t):
    n, k, b, s = [int(s) for s in input().split()]
    answer = solution(n, k, b, s)
    # print("----------------------------", answer)
    print(answer)
