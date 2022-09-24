/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
bool rec(TreeNode*lroot,TreeNode*rroot){
    if(lroot==NULL || rroot==NULL){return lroot==rroot;}
    if(lroot->val != rroot->val){return false;}
    return rec(lroot->left,rroot->right) && rec(lroot->right,rroot->left);
}
public:
    bool isSymmetric(TreeNode* root) {
        return rec(root->left,root->right);
    }
};
