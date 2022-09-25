x,y,z= [int(s) for s in input().split()]

if x < 0:
    x *= -1
    y *= -1
    z *= -1


if y > x or y < 0:
    print(x)
else:
    if z > y:
        print(-1)
    else:
        if z > 0:
            print(x)
        else:
            print(abs(z) * 2 + x)