# Intuition

XXXXXX YYYYYYY
duplicate沒有貢獻, 可以拿掉來看
x1 = set(nums1)
x2 = set(nums2)

首先比較好想到的是:
如果`len(x1) <= n//2 and len(x2) <= n//2`, 代表兩邊光是duplicate, 就能滿足移除掉**n//2**
那max possible set size就是len(x1|x2)

```py
if len(x1) <= n//2 and len(x2) <= n//2:
    return len(x1|x2)
```

再來就是:兩邊各移除掉n//2, 相當於兩邊各自盡量選n//2個distinct number留下
由於我們要盡可能留下較多的distinct number, 如果該num只在其中一邊有, 我們要盡可能留住這些
之後我們再考慮nums1, nums2都共同擁有的數

```py
x1 = set(nums1)
x2 = set(nums2)

distinct1 = x1-x2
distinct2 = x2-x1
```

1. 如果`len(distinct1) >= n//2`:
   - 代表左邊能貢獻滿獨特的 n//2 個, 右邊能至少貢獻x2個, 最多n//2個
   - 左邊跟右邊有重複也沒差, 重複的相當於左邊不拿, 我們改在右邊拿
   - 所以最多能有: n//2 + min(n//2, x2) 個
2. 反之, 如果`len(distinct2) >= n//2`:
   - 代表右邊能貢獻滿獨特的 n//2 個, 左邊能至少貢獻x1個, 最多能n//2個
   - 左邊跟右邊有重複也沒差, 重複的相當於右邊不拿, 我們改在左邊拿
   - 所以最多能有: n//2 + min(n//2, x1) 個
3. 第三種情況, 兩邊的distinct number都少於 n//2
   - greedy來想, 那些只存在於其中一邊的, 我們肯定要盡可能選取, 所以先拿distinct1, distinct2
   - 剩下的空位, 例如:
     - distinct1 = [X X X _ _ _]
     - distinct2 = [Y Y _ _ _ _]
     - nums1還可以再選3個, nums2還可以再放4個
   - 我們就看還剩下幾個distinct number是兩邊都有的, 我們就任意放置在這些位置
   - 所以我們總共能貢獻: `len(distinct1) + len(distinct2) + len(common)`
   - 但別忘記最多就只能貢獻`n`個distinct number (common個數有可能超出剩餘空格)
   - 所以加個上限min(n, len(distinct1) + len(distinct2) + len(common))
   - common = x1 & x2 