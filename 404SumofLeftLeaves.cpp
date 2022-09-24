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
bool isleaf(TreeNode* root){
    if(root==NULL){return false;}
    if(root->left==NULL && root->right==NULL){return true;}
    return false;
}
void dfs(TreeNode* root, int &ans){
    if(root==NULL){return ;}
    if(isleaf(root->left)){ans+=root->left->val;}
    dfs(root->left,ans);
    dfs(root->right,ans);
}
public:
    int sumOfLeftLeaves(TreeNode* root) {
        int ans=0;
        dfs(root,ans);
        return ans;
    }
};
