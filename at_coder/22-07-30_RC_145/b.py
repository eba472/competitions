n, a, b = [int(a) for a in input().split()]
def solve(n,a,b):
    if n < a:
        return 0
    lose = a  - 1
    if a <= b:
        return n - lose
    whole = n // a
    reminder = n % a
    win = b * (whole-1) + min(b, reminder+1)
    return win

print(solve(n,a,b))