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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root!=NULL){bfs(root,1);}
        return ans;
    }
    void bfs(TreeNode* root,int level){
    if(ans.size()<level){
        vector<int> tmp;
        ans.push_back(tmp);
    }            
    ans[level-1].push_back(root->val); 
    if(root->left!=NULL){bfs(root->left,level+1);}
    if(root->right!=NULL){bfs(root->right,++level);}
}
};
