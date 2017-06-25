# Problem: Binary Tree Mode
# (https://leetcode.com/problems/find-mode-in-binary-search-tree/#/description)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        streak = 0
        longestStreak = 0
        lastNumber = None
        res = []
        
        stack = []  # nodes to process
        nextNode = root # node to go to/travel but not process
        while stack or nextNode:
            if nextNode == None:
                processNode = stack.pop()
                nextNode = processNode.right

                if lastNumber != processNode.val:
                    if streak >= longestStreak:
                        if streak > longestStreak:
                            res = []
                            longestStreak = streak
                        res.append(lastNumber)
                    
                    lastNumber = processNode.val
                    streak = 0
                    
                streak += 1
                if not nextNode and not stack and processNode.val != None:
                    stack.append(TreeNode(None))
                continue
            stack.append(nextNode)
            nextNode = nextNode.left
        
        return res
            
            
            