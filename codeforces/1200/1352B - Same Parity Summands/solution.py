t = int(input())
for _ in range(t):
    [n, k] = list(map(int, input().split()))
 
    # try to construct all even number array
    total = n
    arr = [2] * k
    total -= 2*k
    if total >= 0:
        arr[0] += (total // 2) * 2
        total %= 2
        if total == 0:
            print("YES")
            print(" ".join(map(str, arr)))
            continue
 
    # try to construct all odd number array
    total = n
    arr = [1] * k
    total -= k
    if total >= 0:
        arr[0] += (total // 2) * 2
        total %= 2
        if total == 0:
            print("YES")
            print(" ".join(map(str, arr)))
            continue

    print("NO")