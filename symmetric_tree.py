# Problem: Symmetric Tree
# (https://leetcode.com/problems/symmetric-tree/)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Ok, so I actually spent a lot of time on this question because
# my recursion game wasn't strong and I felt like a bumbling idiot...
# Anyway, here's what I got:

# This question can be solved using "symmetric" DFS...in other words, it's TWO
# preorder DFS's at a time, starting from the root for the left and right
# subtrees - the DFS's are "opposite" 

# Each recursive call lets us compare the "matching" or "reflected" pair of nodes
# as we go in the opposite directions for each root for each step, i.e.
# if r1 goes left, r2 goes right and vice versa. Because the paths are mirrored,
# for each step, we are able to compare the "mirrored" node at every step.
# If the mirrored node does not match our conditions, we return FALSE for the inner/outer path.
# if no violations occur and we are at the end of a branch, we return
# the AND of both the inner and outer path.

# The below is a recursive solution. An iterative solution using a stack is also
# implemented.

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.symmetricDFS(root, root)
    
    def symmetricDFS(self, r1, r2):
        if r1 is None and r2 is None:
            # branches ending condition
            return True
        elif (r1 is None and r2 is not None) or (r2 is None and r1 is not None):
            # asymmetry condition
            return False
        elif r1.val != r2.val:
            # asymmetry condition
            return False

        outerSymmetry = self.symmetricDFS(r1.left, r2.right)

        # to prevent traversing the tree again, in the opp direction, from root
        if r1 == r2:
            return outerSymmetry

        innerSymmetry = self.symmetricDFS(r1.right, r2.left)

        return outerSymmetry and innerSymmetry




class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        