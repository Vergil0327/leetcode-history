# Intuition

```py
def __init__(self, arr: List[int]):
    self.arr = arr
    self.presum = [Counter() for i in range(len(arr)+1)]
    for i in range(len(arr)):
        self.presum[i+1] = self.presum[i].copy()
        self.presum[i+1][arr[i]] += 1

def query(self, left: int, right: int, value: int) -> int:
    return self.presum[right+1][value]-self.presum[left][value]
```
最直覺粗暴就是prefix sum全部紀錄下來, 但這樣會需要O(n^2) space導致MLE


但其實我們目標是對特定value做range query, 所以我們可以分別對各個value記錄他們的index位置
然後再配合binary search去搜出那段區間有多少index即可

最後我們只會需要O(n) space, 而時間上也只需要O(n)建構, O(logn)查詢