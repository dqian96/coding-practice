# Problem: Flip binary tree to match preorder traversal
# (https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/)

# Done as part of contest 118

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getNextNode(self, root, isFlip):
        if root is None: return

        yield root

        if isFlip[0] == True:
            temp = root.left
            root.left = root.right
            root.right = temp

        yield from self.getNextNode(root.left, isFlip)
        yield from self.getNextNode(root.right, isFlip)

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        isFlip = [0]
        nodeGenerator = self.getNextNode(root, isFlip)

        flips = []
        for i in range(len(voyage)):
            curr = next(nodeGenerator)

            isFlip[0] = 0

            if curr.val != voyage[i]:
                return [-1]

            if curr.left is not None and curr.left.val == voyage[i + 1]:
                continue
            elif curr.left is None and curr.right is not None and curr.right.val == voyage[i + 1]:
                continue
            elif curr.left is None and curr.right is None:
                continue
            elif curr.left is not None and curr.right is not None and voyage[i + 1] == curr.right.val:
                isFlip[0] = 1
                flips.append(curr.val)
            elif curr.left is not None and voyage[i + 1] != curr.left.val:
                # bad
                return [-1]
            elif curr.right is not None and curr.left is None and curr.right.val != voyage[i + 1]:
                return [-1]

        return flips

