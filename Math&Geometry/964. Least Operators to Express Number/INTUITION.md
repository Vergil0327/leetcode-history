# Intuition

```
Example 1:

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.
```

首先想法是greedily去讓x接近target => 乘法
所以我們透過`y = log(target, x)`可以知道我們需要幾次乘法才可以讓x到target的附近
再來:
1. ceil(y): 會是恰好大於*target*, 此時下個target變成`pow(x, ceil(y)) - target`, 令其為**next_target1**
2. floor(y): 會是恰好小於*target* 此時下個target變成`pow(x, floor(y)) - target`, 令其為**next_target2**

這時發現我們將一個問題變成兩個子問題, 我們在從兩個target取次數最少的: min(leastOpsExpressTarget(x, next_target1), leastOpsExpressTarget(x, next_target2))

所以我們看到這有遞歸性質, 並且由一個問題拆成兩個子問題, 這可以用dynamic programming來解
狀態轉移為:

## 第一種情況: (x * x * ... * x) - leastOpsExpressTarget(x, next_target1)

我們花費了`ceil(y)-1`個乘號, 1個減號 + leastOpsExpressTarget(x, next_target1)個運算符

## 第二種情況: (x * x * ... * x) + leastOpsExpressTarget(x, next_target2)

我們花費了`floor(y)-1`個乘號, 1個加號 + leastOpsExpressTarget(x, next_target2)個運算符

兩者取最小的即可:

```py
y = log(target, x)
l, r = floor(y), ceil(y)

min(self.leastOpsExpressTarget(x, next_target1) + (l-1)+1  if next_target1 < target else inf,self.leastOpsExpressTarget(x, next_target2) + (r-1)+1  if next_target2 < target else inf)
```

*但這邊要注意, 我們的目的是逐漸縮減target, 所以一但next_target1 > target, 那我們不能走這個選項, 直接就返回inf, 不然會導致無限遞歸下去

> 例如. x=5, target=6
> 如果我們選擇5*5 - (25-6) => next_target=19 => 變成leastOpsExpressTarget(5, 19) => 下次又變成leastOpsExpressTarget(5, 6) => leastOpsExpressTarget(5, 19) => ...

因此我們遞歸框架就能寫成:

```py
@cache
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        y = log(target, x)
        l, r = floor(y), ceil(y)
        next_target1 = target-pow(x, l)
        next_target2 = pow(x, r)-target

        return min(self.leastOpsExpressTarget(x, next_target1) + (l-1)+1  if next_target1 < target else inf,
                   self.leastOpsExpressTarget(x, next_target2) + (r-1)+1  if next_target2 < target else inf)
```

那我們該如何結束遞歸? 我們的base case是?

## base case

直覺能想到的就是當`target < x`的時候, 此時我們只能用**x/x=1**來透過加減法抵達target

1. 透過加法, ex. x=5, target=2 => 5/5 + 5/5
   - 我們會有target個1 => **target個**`/`號
   - 會有**target-1次**個`+`號
   - 所以整體運算符為`target+(target-1)`
2. 透過減法, ex. x=5, target=4 => 5-5/5
   - 首先會要減去**x-target個**1, 代表會有**x-target**的減號
   - 由於會有**x-target個**1, 所以會有**x-target個**`/`號
   - 所以整體運算符為`x-target + x-target`

因此:
```py
if target < x:
    # x=5, target=2 => 5/5 + 5/5 => target + (target-1)
    # x=5, target=4 => 5-5/5     => (x-target) + (x-target)
    return min(target + target-1, x-target + x-target)
```
        