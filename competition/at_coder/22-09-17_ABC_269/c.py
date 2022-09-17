a = bin(int(input()))[2:]

ones = []
for i in range(len(a)):
    if a[i] == "1":
        ones.append(i)

possCount = 2 ** len(ones)

l = ["0"] * len(a)
for i in range(possCount):
    o = bin(i)[2:]
    for j in range(-1,- len(o) - 1, -1):
        if o[j] == "1":
            l[ones[j]] = "1"
    print(int("".join(l), 2))

    for j in range(-1,- len(o) - 1, -1):
        if o[j] == "1":
            l[ones[j]] = "0"