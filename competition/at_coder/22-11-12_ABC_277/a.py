n, x = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]


def sol(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i+1


print(sol(a, x))
