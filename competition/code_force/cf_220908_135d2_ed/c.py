def f(a):
    return len(str(a))

def solution(n,a,b):
    cnt = 0
    dicta = {}
    for num in a:
        dicta[num] = dicta.get(num, 0) + 1
    dictB = {}
    for num in b:
        if num in dicta:
            if dicta[num] > 1:
                dicta[num] -= 1
            else:
                del dicta[num]
        else:
            if num // 10 > 0:
                x = f(num)
                cnt += 1
                if x in dicta:
                    if dicta[x] > 1:
                        dicta[x] -= 1
                    else:
                        del dicta[x]
                else:
                    dictB[x] = dictB.get(x, 0) + 1
            else:
                dictB[num] = dictB.get(num, 0) + 1
    # all dictB is single digit
    # print(dicta, dictB, cnt)
    newDictA = {}
    for num in dicta:
        if num // 10 > 0:
            new_num = f(num)
            cnt += dicta[num] 
            count = dicta[num] 
            newDictA[new_num] = newDictA.get(new_num,0) + count
        else:
            newDictA[num] = newDictA.get(num,0) + dicta[num]
    # print(newDictA, dictB, cnt)
    diff_count = 0

    if 1 in newDictA:
        del newDictA[1]
    if 1 in dictB:
        del dictB[1]

    for key in newDictA:
        if key in dictB:
            if dictB[key] >= newDictA[key]:
                dictB[key] -= newDictA[key]
            else:
                dictB[key] = 0
                diff_count += (newDictA[key] - dictB[key])
        else:
            diff_count += newDictA[key]
    # print(dictB)
    diff_count += sum(dictB.values())

    return cnt + diff_count

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]
    ans = solution(n,a,b)
    # print("----------------------------", ans)
    print(ans)
