# Problem: Friend Circles
# (https://leetcode.com/problems/friend-circles/description/) 

# Easy. Find number of connected components via DFS

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        numFriendGroups = 0
        for i in range(len(M)):
            if M[i][i] != -1:
                numFriendGroups += 1
                self.dfs(i, M)
        return numFriendGroups
    
    def dfs(self, i, M):
        if M[i][i] == -1:
            return
        M[i][i] = -1
        for j in range(len(M)):
            if M[i][j] == 1:
                self.dfs(j, M)
        