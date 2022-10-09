class Solution {
public:
    void dfs(vector<vector<char>> &grid,int x,int y){
        if (x<0 or y<0 or x>=grid.size() or y>=grid[0].size() or grid[x][y]=='0'){return;}
        grid[x][y]='0';
        dfs(grid,x-1,y);
        dfs(grid,x+1,y);
        dfs(grid,x,y-1);
        dfs(grid,x,y+1);
    }
    int numIslands(vector<vector<char>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        int count=0;
        for(int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                if (grid[i][j]=='1'){
                    dfs(grid,i,j);
                    count++;
                }
            }
        }
        return count;
    }
};
