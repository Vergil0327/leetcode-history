# Intuition

it looks exactly like dp problem and state transition is VERY clear:
a + e
e + a/i
i + a/e/o/u
o + i/u
u + a

which means:
dp[i+1]["a"] = (dp[i+1]["a"] + dp[i]["e"]) % mod
dp[i+1]["e"] = (dp[i+1]["e"] + dp[i]["a"] + dp[i]["i"]) % mod
dp[i+1]["i"] = (dp[i+1]["i"] + dp[i]["a"] + dp[i]["e"] + dp[i]["o"] + dp[i]["u"]) % mod
dp[i+1]["o"] = (dp[i+1]["o"] + dp[i]["i"] + dp[i]["u"]) % mod
dp[i+1]["u"] = (dp[i+1]["u"] + dp[i]["a"]) % mod

time/space complexity: O(5n)