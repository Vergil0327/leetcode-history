#include <vector>
using namespace std;

class Diff2d {    
public:
    vector<vector<int>>f;
    vector<vector<int>>diff;    
    int m,n;
    Diff2d(int m, int n)
    {
        this->m = m;
        this->n = n;
        diff.resize(m+1);
        f.resize(m+1);        
        for (int i=0; i<m+1; i++)
        {
            diff[i].resize(n+1);
            f[i].resize(n+1);
        }            
    }
    void set(int x0, int y0, int x1, int y1, int val)
    {
        diff[x0][y0]+=val;
        diff[x0][y1+1]-=val;
        diff[x1+1][y0]-=val;
        diff[x1+1][y1+1]+=val;
    }
    void compute()
    {
        f[0][0] = diff[0][0];
        for (int i=0; i<m; i++)
            for (int j=0; j<n; j++)
            {
                int a = i==0?0:f[i-1][j];
                int b = j==0?0:f[i][j-1];
                int c = (i==0||j==0)?0:f[i-1][j-1];                
                f[i][j] = a + b - c + diff[i][j];
            }
    }    
};

class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        Diff2d diff2D(n, n);
        for (const auto& query: queries) {
            int row1 = query[0], col1 = query[1], row2 = query[2], col2 = query[3];
            diff2D.set(row1, col1, row2, col2, 1);
        }
        diff2D.compute();

        vector<vector<int>> res(n, vector<int>(n, 0));
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                res[i][j] = diff2D.f[i][j];
            }
        }
        return res;
    }
};