# Intuition

我們可以這樣定義dp[i][lane]:
dp[i][lane, 1,2,3]: the minimum side jump at position `i` with lane `j`

lane配合obstacles[i]的值，所以我們範圍從1～3

由於要求min jumps, 初始值我們全部都設`inf`
由於i=0時，保證沒有障礙物，所以base case為:
dp[0][1] = 1 # 從lane 2跳過來
dp[0][2] = 0
dp[0][3] = 1 # 從lane 2跳過來

由於如果dp[i][lane]不是障礙物的話
dp[i][lane] = dp[i-1][lane]

*前一個是障礙物的話, 那麼dp[i][lane] = dp[i-1][lane] = obstacle = inf, 一樣合理，必須再透過下面步驟橫跳更新dp*

然後在更新完dp後，每個位置都可以再從另一個不為障礙物的地方橫跳過來
我們可以在試著從這方案選最佳的
dp[i][lane] = min(dp[i][lane], min(dp[i])+1)