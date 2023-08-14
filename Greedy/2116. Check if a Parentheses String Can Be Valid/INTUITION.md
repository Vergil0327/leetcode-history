# Intuition

每個s[i]有三種狀態
- 確定是"(" if s[i] == "(" and locked[i] == 1
- 確定是")" if s[i] == ")" and locked[i] == 1
- locked[i] == 0, 那他可以是"("或")"

s要合法, 那就是遍歷過程中無時無刻左括號都要大於等於右括號
```
()()
(())
((()()))
```
並且最後左右括號要相等

對於locked[i] == 0, 我們可以:
1. 換成"("
2. 換成")"

我們用leftLowerCount跟leftUpperCount代表代表左括號的上下限
- leftLowerCount代表"("最少有幾個
- leftUpperCount代表"("最多有幾個

如果locked[i] == 1:
    - 那就沒有操作可做, 更新leftLowerCount, leftUpperCount
    - s[i] == (, leftLowerCount, leftUpperCount = leftLowerCount+1, leftUpperCount+1
    - s[i] == ), leftLowerCount, leftUpperCount = leftLowerCount-1, leftUpperCount-1
如果locked[i] == 0:
    - 必須是下面操作中的一個
    - 我們可以把locked[i]轉成"(", 那這樣相當於"("的可能上限增加, leftUpperCount += 1
    - 我們可以把locked[i]轉成")", 相當於"("的可能下限減少, leftLowerCount -= 1

而我們紀錄leftLowerCount, leftUpperCount的原因是
在遍歷過程中, "("的數目必須大於等於")"
ex. ()(), (()), ((()()))
所以我們可以透過leftLowerCount, leftUpperCount知道過程中能不能透過locked[i]==0的那些可任意操作的位置來使得整個左右括號平衡

如果過程中`leftUpperCount<0`, 代表我們的")"太多, 多過"("的上限, 直接返回False

而如果過程中`leftLowerCount < 0`, 代表我們其中一個`locked[i]==0`不可以改成")", 得把它改成"(", 這樣一增一減相當於`leftLowerCount += 2`
=> ")" -> 改回狀態未定, leftLowerCount += 1 -> 改成"(", leftLowerCount += 1

那如果過程中都是合法的, 那就看最後leftLowerCount有沒有等於0
- 如果等於0, 那介於[leftLowerCount,leftUpperCount]間的那些可以各自形成pair達到平衡
- 如果leftLowerCount > 0, 代表即使全部locked[i]==0都換成右括號, 左括號仍多於右括號


# Other Solution

也能左右各掃一次判斷左右括號有沒有平衡
1. 先由左往右掃一次判斷左括號數目+`locked[i]==0`數目有沒有辦法平衡
2. 再由右往左掃一次判斷右括號數目+`locked[i]==0`數目有沒有辦法平衡
```py
def canBeValid(self, s: str, locked: str) -> bool:
    def validate(s: str, locked: str, op: str) -> bool:
        bal, wild = 0, 0
        for i in range(len(s)):
            if locked[i] == "1":
                bal += 1 if s[i] == op else -1
            else:
                wild += 1
            if wild + bal < 0:
                return False
        return bal <= wild
    return len(s) % 2 == 0 and validate(s, locked, '(') and validate(s[::-1], locked[::-1], ')')
```