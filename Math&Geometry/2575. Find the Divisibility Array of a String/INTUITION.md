# Intuition

每加上word[i], 當前num = num*10 + int(word[i])

如果num%m == 0，那麼下個位數 num' = num*10 + int(word[i])
我們從前個結果已知num%m == 0, 那麼num*10%m也會為0

如果前個結果num%m == a，那麼num' % m = (num\*10+int(word[i])) % m, 會餘 (a*10+int(word[i]))%m

所以我們只要確認餘數即可

直式除法:

9/3 餘 0
99/3 餘 0
998/3 餘 2

  332_
3 9982
  996
  0022 -> 會發現為前一個餘數*10+int(word[i])在取餘數