# Intuition

我們可以對每個k-size subarray進行操作
為了讓全部最後都變為0, 遍歷到i時必須將nums[i-k+1]透過操作變為0
對於一個區間的同步增減，我們可以用difference array來標記

首先看這段區間{nums[0], nums[1], ..., nums[i-k+1]}, 為了讓nums[0]變為0
我們需要nums[0]次操作, 所以我們在diff[i]標記`+=nums[0]`, 然後再diff[i+k]標記 `-=nums[0]`

再來我們繼續遍歷, diff[i] += diff[i-1]
- 如果`diff[i] == nums[i]`, 代表當前這個nums[i]已經滿足所需操作
- 但如果`nums[i] < diff[i]`, 代表我們在完成前面操作時, nums[i]會被減成負數, 這代表我們沒辦法滿足最終條件, 所以直接返回False
- 又如果當`i+k-1 >= n`時, 如果nums[i] != diff[i], 代表也沒有足夠的k-size subarray來進行操作了, 這時也直接返回False
- 剩下情況我們就繼續操作:
  - 我們繼續透過標記diff array來查看還需要額外進行多少操作來使得nums[i]符合操作數
  - extraOps = nums[i]-diff[i]
  - diff[i] += extraOps
  - diff[i+k] -= extraOps


# Other Solution

```
[X X X X X]
         i
```

我們真正應該關心的是diff
因為我們每次操作，都會是將一個長度為k的sliding window裡的每個數都同步減去一定的操作數
並且為了將最後整個all(nums[i]==0), 每次滿足k-size window時, nums[i-k+1], 也就是最左邊的數值必須透過操作減成0

所以這邊我們用operationsUntilNow紀錄, 如果要將[i-k+1:i)這範圍減為0的所需操作
                      
ex.1
2 2 3 1
i ->
              
一開始i=0, 需要2個操作將nums[i]減去為0
再來i=1, 一樣2個操作可同步降為0
再來i=2, 需要3個操作才能使nums[i]變為0

等到window滿足k個時, 此時nums[i-k+1]應該要減成0
代表requireOperationsUntilNow應該減去nums[i-k+1]

並且因為在nums[i]之前，我們會已經減去requireOperationsUntilNow來讓nums[i-k+1]變為0
所以requireOperationsUntilNow僅需要再額外增加`nums[i] - requireOperationsUntilNow`這次數來讓nums[i]也為能透過操作減成0
                      
所以如果nums[i] < requireOperationsUntilNow的話
代表nums[i]會被減成負數, 應此這狀況直接返回False

但如果如果nums[i] >= requireOperationsUntilNow
那就代表我們可以將nums[i-k+1]減成0,並且整個k-size sliding window內的每個數也會在操作後都>=0

並且就像前面提到的, 我們應該關注我們還需要額外操作多少次數來讓nums[i]=0
為了讓nums[i]也減成0, 我們的requireOperationsUntilNow就要+= nums[i]-requireOperationsUntilNow
                                  
因此整個邏輯是:
1. 如果nums[i] < requireOperationsUntilNow => 返回False
2. 在index=i時, nums[i]會因為前面的操作已經扣掉requireOperationsUntilNow, 所以nums[i] -= requireOperationsUntilNow
3. 還需要額外nums[i] - requireOperationsUntilNow次來讓nums[i]為0 => requireOperationsUntilNow += nums[i] - requireOperationsUntilNow
4. 一但sliding window的size滿足k, 應該將nums[i-k+1]降為0, 所以requireOperationsUntilNow -= nums[i-k+1]
    - 注意這邊的nums[i-k+1]並不一定是原始的nums[i-k+1], 因為nums[i-k+1]也可能因為更早之前的操作而已經降低過, 所以我們前面nums[i]才會 -= requireOperationsUntilNow