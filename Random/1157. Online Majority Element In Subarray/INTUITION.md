# Intuition

一開始想到**Brute Force**方式如下

```py
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.count = defaultdict(list)
        for i, v in enumerate(arr):
            self.count[v].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for num, arr in self.count.items():
            l = bisect.bisect_left(arr, left)
            r = bisect.bisect_right(arr, right)
            if r-l < threshold: continue
            return num
        return -1
```

而這肯定會TLE

這題特別的是, 看一下constraint:
**2 * threshold > right - left + 1**

這限制了每個query區間內, 必定只有一個majority element或是沒有
只會有一個element超過半數

所以這題解法是用random pick, 在合理次數內隨機抽樣
如果抽出來的數透過binary search得到區間內的個數後:
- 如果個數 >= threshold, 代表找到majority element
- 如果個數 < threshold, 那就繼續找

如果一定次數後都沒找到的話, 那就返回`-1`

所以可借用brute force的想法, 用hashmap存下每個arr[i]的所在index
然後再隨機抽樣+binary search來判斷是不是majority element