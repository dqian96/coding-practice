// Delete Operation For Two Strings
// (https://leetcode.com/problems/delete-operation-for-two-strings/description/)

class Solution {
public:    
    int dp(const string& str1, const string& str2, int i, int j, vector<vector<int>>& T) {
      // base cases
      if (i == str1.size()) {
        return str2.size() - j;
      }

      if (j == str2.size()) {
        return str1.size() - i;
      }

      if (T[i][j] != -1) {
          return T[i][j];
      }
      // recursive
      if (str1[i] == str2[j]) {
        return dp(str1, str2, i + 1, j + 1, T);
      }

      int d1 = dp(str1, str2, i + 1, j, T);
      int d2 = dp(str1, str2, i, j + 1, T);

      T[i][j] = (d1 > d2 ? d2 : d1) + 1;
      return T[i][j];
    }

    int minDistance(string word1, string word2) {
        vector<vector<int>> T;
        for (int i = 0; i < word1.size(); i++) {
            vector<int> temp;
            for (int j = 0; j < word2.size(); j++) {
                temp.push_back(-1);
            }
            T.push_back(temp);
        }
        return dp(word1, word2, 0, 0, T);
    }
};
