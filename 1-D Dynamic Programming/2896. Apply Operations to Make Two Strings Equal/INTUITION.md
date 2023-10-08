# Intuition

我們目標是將s1變為s2, 因此我們僅需要關心不相同的字符即可

定義dp[i]: the cost considering arr[:i]

把所有不相同的字符存到`arr`後, 我們兩個操作分別為:
1. 將arr[i]跟arr[j]同時翻轉, 此時cost=x
    - 突破口在於: 我們先不管後面的arr[j], dp[i]就只關注到i-th element即可, 因此對於arr[i]來說, 她所需的cost相當於`x/2`
2. 從arr[i]開始一路翻轉至arr[j], cost = arr[j]-arr[i]
    - arr = [0,5] => 先翻[0,1]->[1,2]->[2,3]->[3,4]->[4,5] => cost = 5-0 並且中間元素都會翻轉兩邊所以最終不變

所以對於dp[i]來說, 他的狀態轉移方程為:
1. 關注i-th element: dp[i] = dp[i-1] + x/2
2. 關注last 2 elements: dp[i] = dp[i-2] + arr[i]-arr[i-1]
兩者取minimum即可

這關係式其實就是house robber
對於i-th element來說:
1. 我們可以選擇花費`x`進行翻轉
2. 可以花費`arr[j] - arr[i]`一路翻轉

# Edge Case
1. 當arr.length為奇數時, 我們沒辦法透過操作來將s1翻轉成s2, 直接返回-1 
2. 當arr.length為0時, 代表s1已經等於s2, 直接返回0