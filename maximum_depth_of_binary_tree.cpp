/*
Problem: Maximum Depth of Binary Tree
(https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Extremely simple recursive solution.
Every child node is an instance of its parent. Add up all these instances.
+1 for a non-null node as it adds 1 to the depth.
0 for null node, obviously.
Recursively add this up.
*/

 #include <vector>
 #include <iostream>
 #include <string>* 

 //Definition for a binary tree node.
 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

int maxDepth(TreeNode* root) {
	if (root == NULL) return 0;
	return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

int main() {
}