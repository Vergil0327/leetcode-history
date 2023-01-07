# Sliding Window + Sorted List

## Intuition

Sliding Window維護indexDiff這個區間，並且透過Sorted List對這個區間做排序
每當有新的`num[i]`加入，便可以在這個有序數組內透過binary search找到一個lowerbound
這時我們要判斷的有兩個，在index沒有越界的情況下:
1. 如果lowerbound (也就是>= nums[i]的數值) 跟 nums[i] <= valueDiff的話，則返回True
2. 第二種可能則是小於lowerbound的後一位數值，如果這個數值跟nums[i] <= valueDiff的話，也返回True

圖示如下:

有序數組: XXXXXX j k nums[i]

- 其中k為binary search的lowerbound，也就是第一個 >= nums[i]的數
- j則為 < nums[i]的數

這兩個數為最有可能與nums[i]相差小於等於 valueDiff的值

## Complexity

- time complexity

$$nlogk$$

- space complexity

$$O(n)$$

# Bucket Sort

## Intuititon

我們也可以將每個數分到一個valueDiff大小的bucket
也就是在同個bucket內的數一定小於valueDiff

所以對於當前的nums[i]來說，有機會相差<= valueDiff的就僅有三種可能:
1. 與nums[i]同bucket的數
2. nums[i]的前一個bucket
3. nums[i]的後一個bucket

因此對於每個nums[i]，相對應分配到的bucket為`nums[i] // valueDiff`
因此我們僅需比對nums[i]與`buckets[nums[i] // valueDiff]`裡的數
以及前後兩個buckets `buckets[nums[i] // valueDiff+1]`, `buckets[nums[i] // valueDiff-1]`裡的數值有沒有小於等於valueDiff即可

另外每當buckets的數量>indexDiff時，代表 nums[i-indexDiff] 已經超出我們的比對範圍，buckets[nums[i-indexDiff]//valueDiff] 這個bucket已經離得太遠必須移除

另外要注意的是 zero division error，因此當valueDiff為0時，對應的bucket number就是`nums[i]`而非`nums[i] // valueDiff`