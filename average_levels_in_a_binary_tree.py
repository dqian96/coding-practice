# Problem: Average Levels in a Binary Tree
# (https://leetcode.com/problems/average-of-levels-in-binary-tree/description/)
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, level, levelSums, levelNumNodes):
        if root == None:
            return
        if level >= len(levelSums):
            levelSums.append(root.val)
            levelNumNodes.append(1)
        else:
            levelSums[level] += root.val
            levelNumNodes[level] += 1
        self.dfs(root.left, level + 1, levelSums, levelNumNodes)
        self.dfs(root.right, level + 1, levelSums, levelNumNodes)
        
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levelSums = []
        levelNumNodes = []
        self.dfs(root, 0, levelSums, levelNumNodes)
        for i in range(len(levelSums)):
            levelSums[i] /= float(levelNumNodes[i])
        return levelSums

            
        
        