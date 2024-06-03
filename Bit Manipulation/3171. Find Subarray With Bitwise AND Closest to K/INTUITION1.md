# Intuition

AND這操作只會越來越小(The AND value of a subarray is non-decreasing.)
所以對於一個nums[i]來說, 最多就30種結果(一次少一個bit)
ex. 例如111111111 => AND => 111111110 => AND => 111111100 => ...

> nums[i] <= 1e9 => log2(1e9) ~ 30

因此我們可以每次都將nums[i]跟之前所有subarray的AND結果進行AND, 並透過hashset去除duplicate
然後遍歷所有可能去找出最小值即可

因此我們用dp儲存所有AND value of subarray, 並遍歷nums[i]
對於當下nums[i], 我們能更新:

```py
# we can AND(nums[i], previous subarray AND value) or AND(nums[i]) only
dp_next = set([nums[i]]) | set([nums[i]&x for x in dp])
```

並持續遍歷所有可能答案, 更新**res**:
```py
for x in dp_next:
    res = min(res, abs(k-x))
```

time: O(30n)