# Intuition

每加上word[i], 當前num = num*10 + int(word[i])

如果num%m == 0，那麼下個位數 num' = num*10 + int(word[i])
我們從前個結果已知num%m == 0, 那麼num*10%m也會為0
所以我們只要確認餘數即可