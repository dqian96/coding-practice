# Problem: Binary Tree Pruning
# (https://leetcode.com/submissions/detail/150532329/)

class Solution(object):
    def pruneTree(self, root):
        # null root
        if root == None: return None

        # prune subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # do not prune root
        if root.val == 1: return root

        # root value is 0
        if root.left is not None or root.right is not None:
            # at least one subtree is not pruned - do not prune root
            return root

        # both subtrees are pruned - prune root
        return None

