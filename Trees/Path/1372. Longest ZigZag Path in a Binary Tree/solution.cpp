class Solution {
public:
    int LEFT=1, RIGHT=-1;
    int dfs(TreeNode* node, int direction, int& length) {
        if (!node) return 0;
        
        int left = dfs(node->left, LEFT, length);
        int right = dfs(node->right, RIGHT, length);

        length = max(length, max(left, right));

        if (direction == LEFT) {
            return right+1;
        } else if (direction == RIGHT) {
            return left+1;
        } else {
            return max(left, right);
        }
    }
    int longestZigZag(TreeNode* root) {
        int res = 0;
        dfs(root, 0, res);
        return res;
    }
};