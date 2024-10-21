# Intuition

由於最後必須是`non-decreasing`, 並且透過操作去將nums[i]除以greatest divisor只會變小
因此我們從後往前遍歷回來, 並且持續進行操作即可

現在問題就只剩如何快速找到greatest divisor?

我們只需要遍歷`[2, sqrt(nums[i])]`這個範圍, 找到的第一個prime factor就會是除以greatest divisor後的nums[i]'

那這樣整體時間複雜度為: O(n*sqrt(nums[i]))