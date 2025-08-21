class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();

        int res = 0;
        for (int top=0; top<m; top++) {
            vector<int> height(n, 0);
            for (int bot=top; bot<m; bot++) {
                for (int col=0; col<n; col++) {
                    if (mat[bot][col] == 1) {
                        height[col]++;
                    }
                }

                int h = bot-top+1;
                int width = 0;
                int cnt = 0;
                for (int col=0; col<n; col++) {
                    if (height[col] != h) {
                        width = 0;
                    } else {
                        width++;
                    }
                    cnt += width;
                }
                res += cnt;
            }
        }
        return res;
    }
};

class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int m=mat.size(),n=mat[0].size();

        for(int i=0;i<m;i++){
            for(int j=n-2;j>=0;j--){
                if(mat[i][j]==1){
                    mat[i][j]+=mat[i][j+1];
                }
            }
        }

        int res=0;
        for(int top=0;top<m;top++){
            for(int j=0;j<n;j++){
                int width=mat[top][j];
                for(int bot=top;bot<m;bot++){
                    width=min(width,mat[bot][j]);
                    res+=width;
                }
            }
        }

        return res;
    }
};

class Solution {
private:
    int histogram(vector<int>& height) {
        int n = height.size();
        vector<int> count(n, 0);

        stack<int> st;
        for (int i=0; i<n; i++) {
            while (!st.empty() && height[st.top()] >= height[i]) {
                st.pop();
            }

            if (!st.empty()) {
                int j = st.top();
                int w = i - j;
                count[i] = count[j] + height[i] * w;
            } else {
                int w = i+1;
                count[i] = height[i] * w;
            }
            st.push(i);
        }
    
        return accumulate(count.begin(), count.end(), 0);
    }
public:
    int numSubmat(vector<vector<int>>& mat) {
        int m=mat.size(),n=mat[0].size();

        vector<int> height(n, 0);
        int res = 0;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (mat[i][j] == 1) {
                    height[j]++;
                } else {
                    height[j] = 0;
                }
            }

            res += histogram(height);
        }
        return res;
    }
};