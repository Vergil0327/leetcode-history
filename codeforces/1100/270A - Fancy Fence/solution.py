# 正多邊形的內角和公式是(n-2) * 180 度，其中n是邊的數量
# 所以每個內角度數為(n-2) * 180 / n
 
n = int(input())
 
for _ in range(n):
    deg = int(input())
 
    if deg < 60: # can't even have a triangle
        print("NO")
    else:
        # (n-2) * 180 / n = deg
        # (n-2) * 180 = deg * n
        # 180*n - 360 = deg * n
        # (180-deg) * n = 360
        n = 360 / (180-deg)
        if n.is_integer():
            print("YES")
        else:
            print("NO")