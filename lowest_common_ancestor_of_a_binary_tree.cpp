/*
Problem: Lowest Common Ancestor of a Binary Search Tree
(https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

It's important to READ the question CAREFULLY, in order to identify PATTERNS.

We are given a BINARY SEARCH TREE, which has the property that
for any parent node A, left child node B, and right child node C,
B <= A <= C.
It's an ordered tree, where the nodes in the left subtree are always smaller 
than the root node, and the nodes in the right subtree are always bigger.

We can use this information to our advantage.
Let the two given nodes be A and B.

Starting from the root, if both A and B are STRICTLY smaller than the root, then we
know that A and B lie in the left subtree. If both A and B are in the left subtree,
then their LCA:

1.Cannot be in right subtree, since A and B are not there.
2.Is not the root node. 
Proof:
Assume the root node is the LCA.
Since both A and B are smaller than the LCA, they
lie in the left subtree of the LCA. 
Since the root node is the LCA, in the left subtree, there is no node parent to both
A and B. 
If there is no node parent to both A and B, then A and B must be in different branches
from the root node. But both are in the same branch. Contradiction.

This means that A,B, and the LCA lie in the left subtree.

Similar reasoning applies for the right if both A and B are bigger than the root.

If neither of the above is true, then we know A and B:

1. Lie in seperate subtrees from the current node, then the LCA cannot
be in either subtree as the other child node is not in said subtree. Therefore,
the current node is the lowest node that is parent to both A and B/subtrees, and thus it is
the LCA.

2. A/B is a child of B/A (current node) is the other case where both
A and B are not in left/right subtrees. In this case, since one node 
is simply the parent of the other, then the parent is the LCA since it is lowest node
parent to both (any lower, and the current node would only be the parent of 1 of them)

Described are two solutions, recursive and iterative. 
*/



#include <iostream>

using namespace std;


//Definition for a binary tree node.
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
/*
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
	if (p->val < root->val && q->val < root->val) {
		return lowestCommonAncestor(root->left, p, q); 
	}
	else if (p->val > root->val && q->val > root->val) {
		return lowestCommonAncestor(root->right, p, q); 
	}
	return root;
}
*/

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
	while (!(min(q->val, p->val) <= root->val && root->val <= max(q->val, p->val))) {
		if (p->val < root->val && q->val < root->val ) root = root->left;
		else root = root->right;
	}	
	return root; 
}

int main() {}