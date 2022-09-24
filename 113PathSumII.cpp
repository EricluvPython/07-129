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
public:
    vector<vector<int>> ans;
    void dfs(TreeNode* root, int totarget, vector<int>&path) {
        if(root==NULL){return ;}
        path.push_back(root->val);
        totarget -= root->val;
        if(root->left==NULL && root->right==NULL){
            if(totarget == 0){ans.push_back(path);}
        }else{
            dfs(root->left, totarget, path);
            dfs(root->right, totarget, path);
        }
        path.pop_back();
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        dfs(root,targetSum,path);
        return ans;
    }
};
