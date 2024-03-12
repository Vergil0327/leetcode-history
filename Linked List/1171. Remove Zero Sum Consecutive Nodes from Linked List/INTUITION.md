# Intuition

### step1

首先我先將linked list轉成array

### step2
再來由於要將sum(subarray)==0的subarray去除, 直覺想到prefix sum + hashmap

因此我們用個hashmap並且紀錄{presum: linked list size}
一開始presum=0且size=0, 因此hashmap初始值為{0:0}

再來遍歷linked list nodes, 並將node加入到`res`裡
一但在hashmap找到相同的`current_presum`, 代表我們只需要linked list只需要保留前面`seen[current_presum]`這段長度
所以我們就將res裡的nodes一個個pop掉, 直到res size == seen[current_presum]
並同時刪除hashmap裡的紀錄

```py
presum = 0
seen = {0:0}
res = []
for node in nodes:
    presum += node.val
    if presum in seen:                
        size = seen[presum]
        presum -= node.val
        while res and len(res) > size:
            del seen[presum]
            presum -= res.pop().val
    else:
        res.append(node)
    seen[presum] = len(res)
```

### step3

最後再將剩餘在res裡的節點還原成linked list即可

Time: $O(n)$
Space: $O(n)$