class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;

        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            // Node to be deleted found
            if (!root->left) return root->right;
            if (!root->right) return root->left;

            // Node with two children: get the inorder successor (smallest in the right subtree)
            TreeNode* successor = root->right;
            while (successor->left) {
                successor = successor->left;
            }
            // Copy the inorder successor's value to this node
            root->val = successor->val;
            // Delete the inorder successor
            root->right = deleteNode(root->right, successor->val);
        }
        return root;
    }
};