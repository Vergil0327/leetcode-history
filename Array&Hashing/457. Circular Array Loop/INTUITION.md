# Two Hashmap
## Intuition

把array想成一個graph，是個可以有多個環的graph
對於每個點我們都進行DFS，把經過的點都記錄到**Hashset** `cycle` 裡，找出當下這個cycle的起始點。同時經過的每個點，也就是目前檢查的這個環加入到另一個**Hashset** `checked` 裡，標註著個環已經檢查過，之後遍歷可以跳過

找到當前cycle起始點 `i` 後，開始DFS

`next node = i + nums[i]`

並且注意DFS的方向必須始終一致，因為在多個點之間來回橫跳並不會形成環
代表DFS過程中，移動方向必須始終一致。
因此這邊我們定義往右移動`direction=1`，往左移動則為`direction=-1`
DFS過程必須保持 `next_direction * direction > 0`

一但往回走，便不可能形成環，直接break，然後檢查下個環
但若成功DFS完一圈後，當環的size `k`大於1的話，代表我們找到合法的環，直接返回**True**

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$

# Follow-Up

## Intuition

使用 slow/fast pointer 技巧，在不允許來回橫跳情況下移動，當兩者相交代表有環的存在，確認其`size>1`(不是self-reference cycle)，即返回**True**

否則則把當前檢查的每個node標記visited，並繼續檢查下個環

*ps. 我們可以標記成`0`代表visited，因為0會形成self-cycle而被判定成**False***

## Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(1)$$