#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    TreeNode *subtreeWithAllDeepest(TreeNode *root)
    {

        function<pair<TreeNode *, int>(TreeNode *)> dfs = [&](TreeNode *node)
        {
            if (!node)
                return make_pair((TreeNode *)nullptr, 0);

            auto left = dfs(node->left);
            auto right = dfs(node->right);

            if (left.second == right.second)
            {
                // Current node is the common ancestor for deepest nodes in both sides
                return make_pair(node, left.second + 1);
            }

            if (left.second > right.second)
            {
                // Deepest nodes are only in the left
                return make_pair(left.first, left.second + 1);
            }
            else
            {
                // Deepest nodes are only in the right
                return make_pair(right.first, right.second + 1);
            }
        };

        return dfs(root).first;
    }
};