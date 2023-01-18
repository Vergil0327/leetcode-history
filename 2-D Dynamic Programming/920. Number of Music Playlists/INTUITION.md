# Intuition

we want to know how many possible playlists with lenth `goal` we can create from `n` songs

and only if we have other `k` songs in playlist, we can put duplicate song in playlist

**Top-Down**

consider `dfs[i][j]` to be **the number of playlists of length `i` that have exactly `j` unique songs**

for a playlist:

if current song is unique (first time we choose), we got `dfs(i+1,j+1) * (n-j)` possible ways to create

**dfs(i+1,j+1)** is the current number of playlists that have `i` songs with `j` uniq song
**n-j** is the rest of possible song we can choose

if current song has been chosen before, we can choose again only if `j>k` which means we've got other `k` songs in playlist

and we got `dfs(i+1, j) * (j-k) if j-k > 0 else 0` ways to create playlist

**dfs(i+1,j+1)** is the current number of playlists that have `i` songs with `j` uniq song
**j-k** is the number of song we can choose again

add them together to get answer:

`dfs(i+1,j+1) * (n-j)` + `dfs(i+1, j) * (j-k) if j-k > 0 else 0`

**Base Case**

`if i == goal, return 1 if j == n else 0` since `every song must be played at least once`.

# Complexity

- time complexity
$$O(goal * n)$$

- space complexity
$$O(goal * n)$$