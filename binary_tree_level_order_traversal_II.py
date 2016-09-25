# Problem: Binary Tree Level Order Traversal II
# (https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

# If an array were given to represent the tree, then this problem
# could be easily solved using index calculations and list splicing.
# Assuming n is the number of nodes and l is the number of levels,
# l = log2(n+1)
# and al is the index of the leftmost node at level l and 
# bl is the index of the rightmost node at level l,
# al = 2^l -1, bl = 2^(l+1) - 2.
# We can use the above arithmetic to reverse iterate the array
# and splice the necessary indices per level in O(n).

# However, we are not given an array but rather nodes.
# Therefore, we simply do BFS through the tree, and add each level
# to the result list.
# We reverse the whole thing after.
# The runtime is O(n), 2 passes in the worst cases (one node per level)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []

        currLevel = [root]
        position = 0
        
        while position < len(currLevel):
            levelValues = []
            lastNodeOnLevel = len(currLevel)
            for i in range(position, lastNodeOnLevel):
                if currLevel[i].left is not None:
                    currLevel.append(currLevel[i].left)
                    levelValues.append(currLevel[i].left.val)
                if currLevel[i].right is not None:
                    currLevel.append(currLevel[i].right)
                    levelValues.append(currLevel[i].right.val)    
            position = lastNodeOnLevel + 1
            
            if len(levelValues) != 0:
                res.append(levelValues)

        res.reverse()
        res.append([root.val])
        return res
