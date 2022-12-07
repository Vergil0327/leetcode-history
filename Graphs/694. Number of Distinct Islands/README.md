[694. Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/)

*[SUBSCRIBE TO UNLOCK](https://leetcode.com/problems/number-of-distinct-islands/)*

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:

11000
11000
00011
00011
Given the above grid map, return 1.

 

Example 2:

11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:

11
1
and

 1
11
are considered different island shapes, because we do not consider reflection / rotation.

 

Note: The length of each dimension in the given grid does not exceed 50.

<details>
<summary>Solution</summary>

```c++
// encode coordinate to string and put string to hashset to prevent duplicate
class Solution {
public:
    vector<vector<int>> dirs{{0,-1},{-1,0},{0,1},{1,0}};
    int numDistinctIslands(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        unordered_set<string> res;
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    set<string> s;
                    helper(grid, i, j, i, j, visited, s);
                    string t = "";
                    for (auto str : s) t += str + "_";
                    res.insert(t);
                }
            }
        }
        return res.size();
    }
    void helper(vector<vector<int>>& grid, int x0, int y0, int i, int j, vector<vector<bool>>& visited, set<string>& s) {
        int m = grid.size(), n = grid[0].size();
        visited[i][j] = true;
        for (auto dir : dirs) {
            int x = i + dir[0], y = j + dir[1];
            if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == 0 || visited[x][y]) continue;
            string str = to_string(x - x0) + "_" + to_string(y - y0);
            s.insert(str);
            helper(grid, x0, y0, x, y, visited, s);
        }
    }
};
```

```c++
class Solution {
public:
    vector<vector<int>> dirs{{0,-1},{-1,0},{0,1},{1,0}};
    int numDistinctIslands(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        set<vector<pair<int, int>>> res;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != 1) continue;
                vector<pair<int, int>> v;
                helper(grid, i, j, i, j, v);
                res.insert(v);
            }
        }
        return res.size();
    }
    void helper(vector<vector<int>>& grid, int x0, int y0, int i, int j, vector<pair<int, int>>& v) {
        int m = grid.size(), n = grid[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] <= 0) return;
        grid[i][j] *= -1;
        v.push_back({i - x0, j - y0});
        for (auto dir : dirs) {
            helper(grid, x0, y0, i + dir[0], j + dir[1], v);
        }
    }
};
```

</details>

<details>
<summary>Explanation</summary>

[labuladong](https://labuladong.github.io/algo/4/31/107/)
</details>