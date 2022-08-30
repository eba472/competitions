
t = int(input())
res = []

def solution(n,k,s):
    if n > 2 * k:
        return False
    
    counter = dict()

    for num in s:
        counter[num] = counter.get(num, 0) + 1
    print("\n----\n", s, counter)
    return all([i <= 2 for i in counter.values()])

for i in range(t):
    n, k = [int(i) for i in input().split()]
    s = [int(i) for i in input().split()]
    
    res.append(solution(n,k,s))
print(res)

with open('output.txt', 'w') as f:
    for i in range(len(res)):
        if res[i]:
            f.write("Case #{}: YES\n".format(i+1))
        else:
            f.write("Case #{}: NO\n".format(i+1))
