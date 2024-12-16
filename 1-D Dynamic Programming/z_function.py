# https://wangwilly.github.io/willywangkaa/2018/03/19/Algorithm-Z-%E6%BC%94%E7%AE%97%E6%B3%95/
"""
如何建立 Z

最簡單的就是使用兩個迴圈, 外層迴圈將整個「P$T」跑過一遍, 內層迴圈則是看看到底 i 位置的後總和與「P$T」的LCP長度為何。 Time

complexity:O(n2)

我們當然可以使用另一種方法讓建立陣列的時間複雜度降低。 此演算法的關鍵在於要維護一個區間[L…R]
R的位置代表由L處之後可以和整個字串最長的前總和重疊到的最後一個位置( 換句話說:[L…R]是整個字串的前綴子字串 ), 若完全不重疊, 則L與R相等。


i為當前位置:

若i>R, 就代表當前i沒有經過任何「P$S」的前綴子字串, 所以重置L與R的位置(L=i,R=i), 經由比對「P$S」的前綴與i之後的前綴, 並找出最長的子字串(R的位置), 計算新的 L 與 R 的位置, 也一併將 Z[i]值算出來(=R-L+1)。

若 i≤R , 令 K=i-L , 再來我們知道 Z[i]≥min(Z[K],R-i+1) 因為String[i…]與String[K…]共同前R-i+1個字元必然為[P$T]的前綴子字串。
現在有兩種情形會發生:
    case1: 若Z[K]<R-i+1:
        代表沒有任何「P$S」的前綴子字串 從 i 位置開始(否則 Z[K] 的值會更大), 所以也意味著Z[i]=Z[K], 還有區間[L…R]不變。
    case2: 若Z[K]≥R-i+1:
        代表String[i…]可以和String[0…] 繼續比對相同的字元, 也就意味有可能拓展[L…R] 區間, 因此, 我們會設 L=i , 接著從 R 之後開始繼續比對「P$S」的前綴子字串, 最後我們會得到新的R, 並更新[L…R] 區間與計算 Z[i] (=R-L+1)。
"""
def z_function(s):
    n = len(s)
    z = [0] * n

    L = R = 0
    for i in range(1, n):
        if i > R:
            L = R = i
            while R < n and s[R-L] == s[R]:
                R += 1
            z[i] = R-L
            R -= 1
        else:
            k = i-L
            if z[k] < R-i+1:
                z[i] = z[k]
            else:
                L = i
                while R < n and s[R-L] == s[R]:
                    R += 1
                z[i] = R-L
                R -= 1
    return z

# 另種實作方式
def z_functionImpl2(s):
    n = len(s)
    l = r = 0
    z = [0]*n

    for i in range(1, n):
        if i < r:
            z[i] = min(r-i, z[i-l])

        while i + z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        if i+z[i] > r:
            l = i
            r = i+z[i]
    return z

def search(text, pattern):
    # Create concatenated string "P$T"
    concat = pattern + "$" + text
    l = len(concat)
 
    # Construct Z array
    z = z_function(concat)
 
    #  now looping through Z array for matching condition
    for i in range(len(pattern)+1, len(z)):
        if z[i] == len(pattern):
            print("found pattern at index:", i-len(pattern)-1)

if __name__ == '__main__':
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    search(text, pattern)
