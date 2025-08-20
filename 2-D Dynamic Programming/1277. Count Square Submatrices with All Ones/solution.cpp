/*
square: 四邊長相等 => 用邊長長度作為特徵值
dp[i][j]: 在(i,j)位置的合法最長邊長

那麼狀態轉移就考慮左邊目前最長, 上方延伸最長多長, 以及左上角整片的合法最長長度

if matric[i][j] == 1: 更新dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

假設dp[i][j] = 2, 代表(i,j)這位置能組出邊長為1跟2兩種正方形 => res += 2
*/

class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();

        vector<vector<int>> dp = vector(m, vector<int>(n, 0));
        int res = 0;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (matrix[i][j] == 1) {
                    int top = i-1>=0 ? dp[i-1][j] : 0;
                    int left = j-1>=0 ? dp[i][j-1] : 0;
                    int topleft = i-1>=0 && j-1 >=0 ? dp[i-1][j-1] : 0;
                    dp[i][j] = min({top, left, topleft}) + 1;
                    res += dp[i][j];
                }
            }
        }
        return res;
    }
};
