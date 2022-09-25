a,b = [int(s) for s in input().split()]
ps = set()
p = [4,2,1]

i = 0
while a > 0 and i < 3:
    if p[i] <= a:
        ps.add(p[i])
        a -= p[i]
    i += 1

i = 0
while b > 0 and i < 3:
    if p[i] <= b:
        ps.add(p[i])
        b -= p[i]
    i += 1

print(sum(ps))