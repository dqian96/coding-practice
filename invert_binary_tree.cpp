/*
Problem: Invert Binary Tree
(https://leetcode.com/problems/invert-binary-tree/)

Inverting a binary tree can be done using both BFS and DFS methods. 

BFS iteratively inverts nodes on the same level/height at a time, from the root.
DFS recursively inverts the children nodes for each subtree at a time.

Both must traverse through the whole tree, being O(n) time.
BFS uses a queue to keep track of the nodes to "expand," increasing space complexity.
DFS uses recursion, which adds more stack frames, increasing space complexity.

DFS is cleaner and shorter but BFS isn't too complex either.

BFS is probably the optimal choice.
*/

#include <vector>
#include <queue>
#include <iostream>
#include <string>

using namespace std;

//Definition for a binary tree node.
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

//DFS
TreeNode* invertTree(TreeNode* root) {
	if (root == NULL) return root;
    invertTree(root->left);
    invertTree(root->right);
    swap(root->left, root->right);
    return root;
}

//BFS
TreeNode* invertTree(TreeNode* root) {
	if (root == NULL) return root;
    int numberOfNodesToTraverse;
    queue<TreeNode*> nodesToTraverse;
    nodesToTraverse.push(root);
    while (nodesToTraverse.size() != 0) {
    	numberOfNodesToTraverse = nodesToTraverse.size();
    	for (int i = 0; i < numberOfNodesToTraverse; i++) {
    		if (nodesToTraverse.front() == NULL) {
    	    	nodesToTraverse.pop();
    			continue;
    		}
    		swap(nodesToTraverse.front()->left, nodesToTraverse.front()->right);
    		nodesToTraverse.push(nodesToTraverse.front()->left);
    		nodesToTraverse.push(nodesToTraverse.front()->right);
    		nodesToTraverse.pop();
    	}
    }
    return root;
}

int main() {

}