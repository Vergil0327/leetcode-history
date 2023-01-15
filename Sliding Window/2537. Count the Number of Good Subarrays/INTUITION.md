# Intuition

看到subarray，首先想到的是能不能用sliding window來解，達到O(n)之類的解法

每加近一個新的數，產生的pairs為window內相同的數的個數:

```
counter = defaultdict(int)
pairs += counter[num]
```

計算完後再把num更新到`counter` hashmap裡

**但最關鍵的點是：我們要怎麼計算subarray個數?**

這邊我們觀察到一但我們的pairs達到至少`k`個時，我們此時的sliding window在往右擴張的所有subarray都會符合這個條件

如果我們用L, R來表示一個Sliding Window
nums = `L XXXXXXX R XXX`
如果[L,R]裡面有剛好`k`個pairs的話，R再繼續往右移的每一個subarray都會符合至少`k`個pairs的條件

因此一但我們sliding window找到至少`k`個後，此時符合條件的subarray有`len(nums)-R`個

這時我們再移動左邊界`L`，然後繼續移動右邊界`R`找到下一個至少`k`個pairs的sliding window跟此時符合的subarray個數 `len(nums) - R'`

最後加總就是我們要的答案

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$