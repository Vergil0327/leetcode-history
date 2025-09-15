# Intuition

If we divide the total number of matches by number of matches per team, we get n/2. 
This means on average, a team has to play a match every n/2 days. Therefore, if there are more teams, the matches for a team are more far apart, making scheduling the matches easier. This also explains why there's no valid schedule for n<=4.

total matches: n * (n-1)
the number of matches per team: (n-1) * 2 (home and away), also means we need these day for each team

therefore, `n * (n-1) / ((n-1) * 2) = n/2` means team needs to play match every `n/2` days on average.

since we don't allow team play in consecutive days, which means n/2 must greater than 2 to avoid play 2 days consecutively

n/2 > 2 => `n > 4` is the base condition we need to follow

then, solution tells us to do kind of brute force using randomization, :(