# Problem: Binary Tree Level Order Traversal
# (https://leetcode.com/problems/binary-tree-level-order-traversal/)


# Level order traversal (traversal level by level) is simply BFS.
# This is implemented using a queue. Extremely straightforward.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []
        # position of current traversal
        levelPosition = 0
        # number of nodes on level
        levelSize = 1
        
        queue = [root]
        res = []

        while queue:
            if levelPosition == levelSize:
                # done expanding prev level
                res.append(queue)
                levelPosition, levelSize = 0, len(queue)
            else:
                if queue[0].left is not None:
                    queue.append(queue[0].left)
                if queue[0].right is not None:
                    queue.append(queue[0].right)
                queue.pop()
                levelPosition += 1
        return res
