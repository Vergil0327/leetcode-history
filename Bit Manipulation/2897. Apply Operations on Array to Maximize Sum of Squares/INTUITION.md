# Intuition

```
    -> AND   OR
0 1     0    1
1 0     0    1
0 0     0    0
1 1     1    1
```

1只是透過**OR**轉移到updated value
num1 + num2 = AND + OR, 1的總和不變
透過1集中到新的updated value, 我們能得到更大的平方和

x^2 + y^2 vs (x+d)^2 + (y-d)^2 = x^2 + y^2 + 2*d*(x-y) + 2d^2
當 x > y and d > 0 => 右側平方和更大
所以每當做一次操作, 藉由1集中到updated value, 平方和就會增加

所以我們把所有nums[i]的每個bit位都先算出來有多少個
然後bit位上能分配1就分配, 構造出前k大的元素即可

