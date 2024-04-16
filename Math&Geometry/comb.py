## Helper function Cmn

# 1. 預處理Cmn

m = n = 1001
comb = [[0]*n for _ in range(m)]

for i in range(m):
    comb[i][i] = comb[i][0] = 1
    for j in range(1, i):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]



# 2. 直接計算Cmn

def Cmn(m, n):
    cnt = 1
    for i in range(n):
        cnt *= m - i
        cnt /= i + 1
    return cnt

