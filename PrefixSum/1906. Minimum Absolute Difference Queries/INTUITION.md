# Intuition

constraint: 1 <= nums[i] <= 100

=> 把分成100個bucket, 把nums全分類到bucket裡
對於queries[i] = [l, r], 我們可以反過來遍歷這些buckets (最多就100個)並看這些bucket內有沒有在[l,r]這範圍內的index
這樣我們就能以O(max(nums))的時間找到queries[i]區間有哪些值並找出他們的min absolute difference

首先分類過程中bucket內的index會是有序的
```py
buckets = [[] for _ in range(max(nums)+1)]
for i in range(n):
    buckets[nums[i]].append(i)
```

所以再來我們就看bucket跟[l, r]有沒有交集
對於確認區間, 我們可以用:
1. segment tree O(n)時間預處理, O(log(n))時間check
2. prefix sum: O(n)時間預處理, O(1)時間check

用prefix sum的話, 出現的index我們設為1, 所以prefix[index]代表[0,index]這段index區間內有出現多少個index
那這樣我們就能透過presum[r]-presum[l-1]來得知[l,r]這區間有多少個index, 如果**相減大於0**, 就代表存在

每個bucket都要預先處理出他們各自的prefix sum, 所以我們可以定義:
presum[v][i]: 數值為v的bucket, 他的[0:i]的prefix sum

**預處理**
```py
presum = [[0]*n for _ in range(101)]
for v in range(1, 101):
    for i in range(n):
        if nums[i] == v:
            presum[v][i] = (presum[v][i-1] if i-1 >= 0 else 0) + 1
        else:
            presum[v][i] = (presum[v][i-1] if i-1 >= 0 else 0)
```

[Great Explanation from HuifengGuan](https://www.youtube.com/watch?v=UAfiZCuTNAA&ab_channel=HuifengGuan)

# Complexity

- time: O(100 * queries.length + 100 * nums.length)