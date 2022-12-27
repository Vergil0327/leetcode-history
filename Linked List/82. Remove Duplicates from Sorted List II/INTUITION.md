# Stack
## Intuition

額外開個Stack，每次都跟上一個加入的Node比對看有沒有重複
有重複則移除並且不再加入該數值的ListNode
最後將儲存在Stack內未重複的ListNode合併回Linked List即可

**注意在跳出循環後還得再檢查一次是不是該移除Stack內的Node**

edge case: [1,1]

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

# Space-Optimzied

## Intuition

設curr = head
在確保curr 與 curr.next 不為空情況下，判斷兩者是不是相同
- 如果不相同，將`curr`加到dummy node
- 如果相同，移動 `curr` 直到下個不重複的node
- 由於我們的while條件為確保 `curr` 及 `curr.next` 不為None，因此最後記得把最後一個`curr`加到dummy node上

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$