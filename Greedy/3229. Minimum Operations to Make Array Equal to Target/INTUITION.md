# Intuition

這題其實是1526. Minimum Number of Increments on Subarrays to Form a Target Array的follow-up

如果不知道[1526. Minimum Number of Increments on Subarrays to Form a Target Array](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/)的話那這題可能有點難解


先看example 1.

nums:   [3,5,1,2]
target: [4,6,2,4]
=> diff:[1,1,1,2]

直覺想到的是每個**diff > 0**跟**diff < 0**的區間都能一併處理
最終讓diff變為[0, 0, 0, ...]

因此我們就分成`+diff`跟`-diff`區兩種情況處理
但其實`-diff`只是操作不同, 我們取絕對值後他其實整個操作上就跟`+diff`是一樣的
所以我們如果能知道minimum operation of `+diff` subarray, 那負數部分也就迎刃而解

而*1526. Minimum Number of Increments on Subarrays to Form a Target Array* 就是僅有正數的部分

我們先看正數: [1, 1, 2, 3, 2, 5, 1]
最小操作是什麼?

 [1, 1, 2, 3, 2, 5, 1]
 -> [0, 0, 1, 2, 1, 4, 0]
 -> [0, 0, 0, 1, 0, 3, 0]
 -> [0, 0, 0, 0, 0, 2, 0]
 -> ...

 其實就是每個subarray我們都找出他的minimum然後同步一起扣掉
> 所以是可以透過segment tree配合divide and conquer (recursion)來做的

但我們也能利用greedy的方式來處理

一樣用這個做例子:  [1, 1, 2, 3, 2, 5, 1]
我們一開始require_step=0, current_operation=0

步驟如下
1. 一開始元素為1, 所以require_step += 1 - current_operation = 1, 這時更新current_operation=1
2. 再來又碰到1, 這跟我們目前操作的current_operation一樣, 所以實際上是與前個元素一起操作的
3. 然後是2, require_step += 2 - current_operation, 這時我們在更新current_operation = 2
4. 再來3, 所以一樣我們需要額外的操作去將3降為0, require_step += 3 - current_operation, 然後在更新current_operation = 3
5. 這時遇到2, 2 已經小於 current operation, 代表其實2在前面的操作就已經同步降至0了, 所以從2開始會是另一個同步操作的group, 所以更新current_operation = 2

這邊再回頭看一下:

[1, 1, 2, 3, 2, 5, 1]
-> [0, 0, 1, 2, 1, 4, 0]
-> [0, 0, 0, 1, 0, 3, 0]

實際上我們操作過程中, 我們將前個元素`3`降為0時, 這時2會降為1, 實際上我們要處理的subarray會是以2這元素為開頭
所以我們的current_operation會是2, 然後再依序往後看

6. 再來是5, require_step += 5 - current_operation, 在更新current_operation = 5

如此一來, 最終的require_step就是我們要將所有正數的subarray降為0的最少操作

而負數僅需要取絕對值再來一次即可

所以實際上我們在操作的時候, 我們所有遞增序列, 其實我們在紀錄require_step的同時, 也代表我們已經將這些序列都處理完了
而遇到遞減元素的時候, 實際上他必定跟先前的某個subarray一同操作, 所以我們不會額外增加require_step
但current_operation必須更新成該遞減元素, 因為這時考慮的同步操作的subarray已經跟前個元素的subarray不同了

ex. [1,2,3,1, ...], 我們前面[1,2,3]都作為同個group同步decrease:

dec操作如下:
1. [-1, -1, -1, -1, ...]
2. [0, -1, -1, 0, ...]
3. [0, 0, -1, 0, ...]

所以實際上第四個元素是跟第一個元素作為同個subarray同步進行dec操作的, 所以require_step已經計算過了
而current_operation要更新為當前元素然後繼續往後看

如果不懂
greedy solution的說明可另外參考[Huifeng Guan](https://www.youtube.com/live/LA8NMbeF4Xg?si=uNw4ki8c-ptgT0QD&t=1527)的解說


因此, 我們這個greedy solution就分別應用到正數subarray區間跟負數subarray區間即可

```py
requireStep = i = 0
while i < n:
    num = target[i]-nums[i]
    if num == 0:
        i += 1
        continue

    if (curSign := sign(num)) > 0: # dec step
        # 找出連續正數區間操作
        curStep = 0
        j = i
        while j < n and sign(target[j]-nums[j]) == curSign:
            diff = target[j] - nums[j]
            if diff > curStep:
                requireStep += diff-curStep
            curStep = diff
            j += 1
        i = j
    else: # inc step

        # 找出連續負數區間操作, 取絕對值轉成正數後操作
        curStep = 0
        j = i
        while j < n and sign(target[j]-nums[j]) == curSign:
            diff = abs(target[j]-nums[j])
            if diff > curStep:
                requireStep += diff - curStep
            curStep = diff
            j += 1
        i = j
return requireStep
```