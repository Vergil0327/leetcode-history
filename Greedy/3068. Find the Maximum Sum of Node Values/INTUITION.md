# Intuition 1

對任意數XOR兩次相當於沒有操作
A XOR B XOR B = A

所以不止邊, 其實我們可以透過複數操作使得任意兩個節點進行XOR操作, 中間連接的邊都可以透過複數操作使其不變

那既然一次可以對任意兩節點進行XOR操作, 我們就看哪些節點進行XOR操作後會變更大
我們將增加的這個delta 增量排序, 一對一對從大到小的取來找出全局最大的最佳解

# Intuition 2

還有另外一種想法是, 我們看一下nums[i]^k > nums[i]的有幾個
如果是偶數個, 你會發現我們可以透過任意操作組合使這些節點全部轉為nums[i]^k
我們就直接返回: sum(max(num, num^k) for num in nums) 即可

但如果有奇數個, 由於我們都是成對成對的進行操作, 那就代表:
有個節點辦法nums[i]轉為nums[i]^k
或是有個nums[i]^k節點沒辦法轉為nums[i]

那既然要犧牲一個節點, 我們就犧牲變量最小的那個: sacrifice = min(abs(num - (num^k)) for num in nums)
答案就是多扣掉這個變量即可: sum(max(num, num^k) for num in nums) - sacrifice
