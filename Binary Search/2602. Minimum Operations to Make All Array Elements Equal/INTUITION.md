# Intuition

對於每個queries[i]，我們要求的就是每個nums[i]對queries[i]的差的總和

所於首先想到brute force該怎麼做?
兩層循環然後算出差值再加總

再來想到的是我們可以sorting + binary search找到`>= queries[i]`的位置
這樣最佳操作數就是左半邊跟右半邊個別總和減去透過操作轉為queries[i]的總和的差

以下面這個為例
nums = [3,1,6,8]
sorting = [1,3,6,8]
presum = [0,1,4,10,18]
queries= [1,5]

當queries[i] = 5時
我們可以透過binary search找到i=2為 `>= queries[i]` 的位置
所以abs(sum([0:i]) - queries[i]*len([0:i])) + abs(sum[i:n-1] - queries[i] * len(i:n))即為最佳操作數

由於我們需要用到區間和，所以我們可以事先計算prefix sum來幫助我們以O(1)時間計算區間和

