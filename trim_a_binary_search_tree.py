# Problem: Trim a Binary Search Tree
# (https://leetcode.com/problems/trim-a-binary-search-tree/description/)

class Solution(object):
    def trimBST(self, root, L, R):
        if root is None:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
            