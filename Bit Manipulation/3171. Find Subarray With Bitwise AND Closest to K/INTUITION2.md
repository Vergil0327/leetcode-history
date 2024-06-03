# Intuition

另種比較直覺能想到的方式是, 看到subarray, 先想看看sliding window
由於AND只會越AND越小, 所以k-AND(subarray)會逐漸變大

nums[i] <= 1e9 => 最多 m=log2(1e9)個bit

所以一開始持續移動右指針`r`, 在遍歷nums[r]時, 我們遍歷m個bit, 並記錄當前sliding window每個bit[pos]的數目

> 我們用一個bits array `bit`來記錄每個位置的bit有多少個

一旦AND(sliding window)變得太小了, 我們就移動左指針`l`, 並更新每個bit[pos]的數目
然後我們持續維護我們的`current = AND(sliding window)`

移動左指針是因為: 由於AND的性質會使得`AND(nums[l+1:r]) >= AND(nums[l:r])`, 所以當AND(nums[l:r])太小時, 移動`l`至`l+1`去縮小sliding window
並由於我們將nums[l]移出sliding window, 所以我們要重新更新`current`

> 當我們移動左指針一步時, 此時sliding window的長度為r-l, 當前window為[l+1:r] both inclusive
> X {X X X X X X X X X X}
> l                    r


只有當該bit的數目等於sliding window的長度時(為r-l個時), 該bit[pos]才會貢獻AND value
所以反過來說當我們將左指針`l`往右, 一但我們將nums[l]移除sliding window
這時如果有任一bits[pos] == slidwing_window.length了, 那我們就要更新`current`, 把該位置的bit給還原回來

time: O(30n)