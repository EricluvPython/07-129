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
bool dfs(TreeNode*root,int target){
    if(root==NULL){return false;}
        if(root->left==NULL && root->right==NULL){
            return (target-root->val==0) ? true : false;
        }   
        return (dfs(root->left,target-root->val) || dfs(root->right,target-root->val));
    }
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        return dfs(root,targetSum);
    }
};
