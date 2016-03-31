/*
Problem: Same Tree
(https://leetcode.com/problems/same-tree/)

To verify that trees p and q are the same, we must traverse every node of
one tree.
We can stop after nodes don't match to prove that the trees are different,
but to prove that the trees are the same we have to traverse every node of one tree.

This can be done through DFS and BFS.

*/


#include <string>
#include <iostream>
#include <vector>

using namspace std;

//Definition for a binary tree node.
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool isSameTree(TreeNode* p, TreeNode* q) {
	if(p == NULL && q == NULL) return true;
	if (p == NULL && q != NULL || p != NULL && q == NULL || p->val != q->val ) return false;
	return (isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
}

int main() {}