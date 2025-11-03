# Intuition

看到這規模數據`1 <= di <= 10^9`, 先想到用binary search去猜測valid minimum time
這樣問題就轉成如何去確認在`t`底下是否能完成整個過程

- At hours divisible by lcm(r1, r2), both drones are recharging (unavailable).
- For a fixed T, recharge counts are floor(T / r1) and floor(T / r2).
- Available hours: c1 = T - floor(T / r1), c2 = T - floor(T / r2); shared hours = T - floor(T / r1) - floor(T / r2) + floor(T / lcm(r1,r2)).

這題其實就是[2513. Minimize the Maximum of Two Arrays](https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/)的敘述變化題

對於每個猜測的時間`t`來說:

1. drone1需要recharge: t//r1 次, 所以available hours = t - t//r1. 並且由於每次操作所需單位時間都是1, 所以available hours必須滿足:
t - t//r1 >= d1

2. 同樣地, drone2需要recharge: t//r2 次, available hours = t - t//r2 => 必須滿足 t - t//r2 >= d2

3. 但別忘了, 兩台drone不可同時休息, 所以找出最小公倍數LCM = r1 * r2 // gcd(r1, r2) 後, 必須滿足 t - t//LCM >= d1 + d2

> t扣除掉兩台重疊的時間後, 必須足夠總遞送次數`d1 + d2`

所以我們的helper function **check**要檢查的就是當前時間`t`是否能滿足以上三個條件