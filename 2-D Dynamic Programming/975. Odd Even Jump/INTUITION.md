# Sorted List
## Intuition

先以O(nlogn)時間找出每個位置的nextSmaller跟nextGreater

我們可以由後往前找，維護一個有序array(java treemap, c++ map, set, python sorted list)找出每個index的下一個next smaller/next greater index

然後在用dfs去看模擬每個位置能不能跳到`n-1`位置即可

由於是奇數->偶數->奇數跳，所以實際上就是看能不能nextGreater -> nextSmaller -> nextGreater跳到`n-1`

## Complexity

- time complexity:

$$O(nlogn + n)$$

- space complexity:

$$O(n)$$

# Monotonic Stack

## Intuition

既然是要找nextSmaller跟nextGreater，我們可以想到利用monotonic stack來找

但由於我們要找的是對於當前位置`i`的後面整個arr裡的`最小 nextSmaller 跟 nextGreater`

ex. arr = [10,13,12,14,15]
對於 i=0來說，nextGreater[j]是12而非13

因此找的方式跟一般利用monotonic stack找nextSmaller 跟 nextGreater些微不一樣

首先 nextGreater 跟 nextSmaller初始化為自己的index，因為後續我們會判斷，如果nextSmaller或nextGreater指向自己的話，說明無法再往前

- 找nextGreater
  1. 首先對arr由小到大排序:
    ```py
    sorted([[val, i] for i, val in enumerate(arr)])
    ```
  2. 再來我們持續把index加入到stack裡，一但stack[-1] < current index，說明我們找到了stack[-1]的nextGreater的位置

- 找nextSmaller

  1. 同上概念，對arr由大到小排序
    ```py
    sorted([[-val, i] for i, val in enumerate(arr)])
    ```
  2. 一樣持續把index加入到stack裡，一但stack[-1] < current index，說明我們找到了stack[-1]的nextSmaller的位置

找到nextSmaller跟nextGreater後剩下是DFS去看能不能走到最後了

## Complexity

- time complexity:

$$O(nlogn + n)$$

- space complexity:

$$O(n)$$

# Most Optimized Solution

[Lee215](https://leetcode.com/problems/odd-even-jump/solutions/217981/java-c-python-dp-using-map-or-stack/)

這邊巧妙的是，當找完nextSmaller跟nextGreater

我們可以由後往前掃一遍看說當前位置的nextSmaller跟nextGreater能不能走到n-1
類似DP的概念持續更新狀態

最後由於每個位置都是先奇數跳，所以統計oddJump array裡有多少可以跳到`n-1`即為答案

## Code

```py
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nextGreater, nextSmaller = [0] * n, [0] * n

        # 由小到大排列
        increasingArr = sorted([[v, i] for i, v in enumerate(arr)])
        stack = []
        for num, idx in increasingArr:
            while stack and stack[-1] < idx:
                nextGreater[stack.pop()] = idx
            stack.append(idx)

        # 數值由大到小排列，當stack[-1] < idx 代表找到下一個小的位置
        decreasingArr = sorted([[-v, i] for i, v in enumerate(arr)])
        stack.clear()
        for num, idx in decreasingArr:
            while stack and stack[-1] < idx:
                nextSmaller[stack.pop()] = idx
            stack.append(idx)

        oddJump = [0] * n
        evenJump = [0] * n
        oddJump[n-1] = evenJump[n-1] = 1 # base case
        for i in range(n-2, -1, -1):
            # 奇數跳過去後看偶數跳能不能跳到n-1
            oddJump[i] = evenJump[nextGreater[i]]

            # 偶數跳過去後看奇數跳能不能跳到n-1
            evenJump[i] = oddJump[nextSmaller[i]]

        return sum(oddJump) # 看最後每個位置從奇數跳開始能不能跳到最後
```
