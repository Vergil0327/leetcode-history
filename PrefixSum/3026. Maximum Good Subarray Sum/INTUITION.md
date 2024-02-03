# Intuition

首先題意我們只關切|num[i]-nums[j]| == k
絕對值可拆分成:
    1. nums[i]-nums[j] = k
    2. nums[i]-nums[j] = -k
我們就能得到
    1. num[j] = nums[i] - k
    2. nums[j] = nums[i] + k
    
所以我們只要用個hashmap紀錄過往的nums[i], 我們就能透過nums[i]-k跟nums[i]+k確認有沒有nums[j]存在
至於hashmap該存什麼值, 由於我們想要的是maximum subarray sum, 所以我們nums[j]記錄的應該是在nums[j]之前的prefix sum
由於可能有複數個nums[j], 並且我們要maximum subarray sum, 所以在更新hashmap時我們對prefix sum的值取min
這樣`presum_i - hashmap[nums[j]] where nums[j] = nums[i]-k or nums[i]+k`時, subarray sum才會盡可能的大
找的過程中, 在取全局最大`res`即可
        