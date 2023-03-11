# C m 取 n = 包含元素x + 不包含元素x = C m-1 取 n-1 + C m-1 取 n
# m! / n! / (m-n)!
@lru_cache(None)
def Cmn(m, n):
    if n > m-n:
        return Cmn(m, m-n)
    if n == 0: return 1
    if n == 1: return m
    return (Cmn(m-1, n-1) + Cmn(m-1, n))%MOD

"""
C m 取 n = m! / n! / (m-n)!
但如果數值很大又要取MOD的話, 除法並沒有任何取餘數的特性
因此我們可以用另一種組合數的遞歸表達式來計算
`C(m, n) = C(m-1, n-1) + C(m-1, n)`

他的意思是, C m 取 n 就相當於 在m個數內挑取n個時, `一定包含任意元素x`加上`一定不包含任意元素x的組合`
- 一定包含元素x就代表是: C(m-1, n-1) (有一個已經確定是元素x)
- 一定不包含元素x則為: C(m-1, n) (m個裡面剔除掉元素x)

**Base Case**
1. C(m, 0) = 1
2. C(m, 1) = m
3. 另外C m 取 n的個數跟 C m 取 (m-n)的組合數是相同的, 因為挑出n後, 剩下的m-n也就確定沒挑到了
所以 `C(m, n) = C(m, m-n) if n > m-n`
這樣我們能確保m比n大, 一定會走到前面兩個base case而非m先為0


"""