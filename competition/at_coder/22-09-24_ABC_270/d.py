n,k= [int(s) for s in input().split()]
a= [int(s) for s in input().split()]

a.sort(reverse=True)
def sol(n,k,a):
    i = 0
    s = 0
    take = 0
    while i < len(a):
        if a[i] > n:
            i += 1
        else:
            hm = n // a[i] 
            n -= a[i] * hm
            if take % 2 == 0:
                s += a[i] * (hm // 2 + hm % 2)
            else:
                s += a[i] * (hm // 2)
            take += hm
            i += 1
    return s
print(sol(n,k,a))