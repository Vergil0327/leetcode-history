"""
單純分情況討論即可
"""

x1, y1, x2, y2 = list(map(int, input().split()))

# Note that x3, y3, x4, y4 must be in the range ( - 1000 ≤ x3, y3, x4, y4 ≤ 1000).
inRange = lambda x: -1000 <= x <= 1000

# 1. on same horizontal line
if y1 == y2:
    d = abs(x2-x1)
    
    y3 = y1+d
    y4 = y1-d
    if inRange(y3):
        print(x1, y3, x2, y3)
    elif inRange(y4):
        print(x1, y4, x2, y4)
    else:
        print(-1)

# 2. on same vertical line
elif x1 == x2:
    d = abs(y2-y1)

    x3 = x1+d
    x4 = x1-d

    if inRange(x3):
        print(x3, y1, x3, y2)
    elif inRange(x4):
        print(x4, y1, x4, y2)
    else:
        print(-1)
else: # diagnal
    x3, y3 = x1, y2
    x4, y4 = x2, y1
    
    if abs(x1 - x2) == abs(y2-y1):
        print(x3,y3,x4,y4)
    else:
        print(-1)