# Intuition

因為這題`n`的數據範圍很小`<=14`
首先想到的就是bitmask dp

**topdown-dp**

我們用bitmask來紀錄我們選的狀態
再來我們就開始建構這個permutation

只要當前的nums[i]沒有被選過並且他跟前一個選擇為倍數關係(nums[i]%prev == 0 or prev%nums[i] == 0)

那麼nums[i]就是合法的建構, 我們就能繼續透過dfs建構下去

一但每個數都有選到, 那就是個合法的建構

所以我們的dfs必須紀錄`bitmask`跟前一個選擇`prev`

dfs(bitmask, prev)