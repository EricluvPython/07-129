class Solution {
public:
    int longestPalindrome(string s) {
        int ans = 0, f = 0;
        map<char,int>mp;
        for(int i = 0;i < s.size();i++){mp[s[i]]++;}
        for(auto it : mp){
            ans += it.second/2;
            if(it.second % 2 == 1)f = 1;
        }
        return f > 0 ? 2*ans+1 : 2*ans;
    }
};
