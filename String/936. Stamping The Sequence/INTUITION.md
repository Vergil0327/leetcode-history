# Intuition

```
s = ? ? ? ? ? ? ? ? ?
    S T A M P
      S T A M P
```

我們目標是要讓s[i]最後一次被覆蓋的是target[i]
從????? -> target有很多種可能路線
首先想到的是有沒有辦法從target反推回去一種可能

因為最後一次一定是stamp整個覆蓋上去, 所以target一定有一個**substring == stamp**
ex. target = XXXXX stamp XXXX
再來會剩下兩個子區段, 我們一樣繼續找有沒有哪部分的substring是substring of stamp, 繼續標記反推回去, 所以我們可以用遞歸去做

由於我們是逆著推回去, 一但XXXXX被stamp覆蓋, 我們可以想成這段區間變成*****, 可以任意配對任何字母(因為最後都會被覆蓋)

也就是類似這樣
```
round-1: target = XXXXX stamp  XXXX
round-2: target = XXsta *****  XXXX
round-3: target = st*** *****  XXXX
round-4: target = ***** ****(s)tamp => 等到最後變成***** ***** ****, 就代表我們找到一組合法操作序列
```

而且這時會發現, 一但我們標記了stamp那段區間, 就永遠不會被後續操作給覆蓋掉(因為我們是逆推回去的)
所以我們只要盡可能地將target全數標記成`*`號即可, 整體框架如下

```py
def dfs(s):
    if s[0] == "*" and len(set(s)) == 1: return []

    for i in range(n):
        if check(s, i):
            arr = dfs(s[:i] + "*"*len(stamp) + s[i+len(stamp):])
            if arr and arr[0] == "RETURN": return ["RETURN"]
            return arr + [i]

    return ["RETURN"] # 代表無解
    
ans = dfs(target)
return ans if ("RETURN" not in ans) and (len(ans) <= 10*n) else []
```

至於helper func `check`, 目的就是檢查是否可以合法stamp即可

```py
def check(target, start):
    valid = False
    for i in range(len(stamp)):
        if start+i >= n: return False
        if target[start+i] == "*": continue
        if target[start+i] != stamp[i]: return False
        valid = True
    return valid
```

注意不可寫成下面形式, 因為有可能target[start:start+len(stamp)]這段都是由"*"組成
那代表這段已經不需要在stamp了, 應該返回False才對

```py
def check(target, start):
    for i in range(len(stamp)):
        if start+i >= n: return False
        if target[start+i] == "*": continue
        if target[start+i] != stamp[i]: return False
    return True
```