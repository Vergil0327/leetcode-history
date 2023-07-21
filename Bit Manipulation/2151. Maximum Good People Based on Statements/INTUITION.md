# Intuition

- statements[i][j] == 2時, 沒有參考價值, 不予理會
- statements[i][j] == 1時, j是good person, 並且i可能是good person或是bad person講實話
- statements[i][j] == 0時, 重點是這個說人bad的人:
    - 這時假設i是good => j的說詞statements[j][y]都必須重新檢視, 任何說j的說詞statements[x][j]也要重新檢視
    - 以及i是bad => tell truth, 同上
                => tell lie, statements[j][y], statements[x][j]都是對的

由於n <= 15, 所以我們可以用bitmask來表示哪些人是good, 哪些人是bad, 總共就1<<n, 最多32768狀態
然後我們遍歷這些狀態, 找出當前狀態的好壞人
```py
for state in range(1<<n):
    good, bad = set(), set()
    for i in range(n):
        if (state>>i)&1:
            good.add(i)
        else:
            bad.add(i)
```

再來就再透過O(n^2)來驗證說詞
由於bad person可說真話可說假話, 沒有參考價值
我們只需要看那些說真話的人他們的statements[i][j]有沒有矛盾即可
所以在i是好人的情況下:
1. 如果i説j是壞人, 但j其實是好人, 那麼代表i是好人這點是矛盾
2. 如果i説j是好人, 但j其實是壞人, 那麼代表i是好人這點是矛盾

一但說詞都沒有矛盾, 那我們就能更新res = max(res, goodPeople) where goodPeople = number of 1-bit in current state