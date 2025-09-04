n, a, b, c = list(map(int, input().split()))
 
# define dp[i]: the maximum cutting for length i
# state transfer: dp[i] can be transferred from dp[i-a] / dp[i-b] / dp[i-c]
 
dp = [-float('inf')] * (n+1)
dp[0] = 0 # zero cutting for zero length
for i in range(1, n+1):
    if i-a >= 0:
        dp[i] = max(dp[i], dp[i-a]+1)
    if i-b >= 0:
        dp[i] = max(dp[i], dp[i-b]+1)
    if i-c >= 0:
        dp[i] = max(dp[i], dp[i-c]+1)
    
print(dp[n])