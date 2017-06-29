// Problem: Minimum Depth of Binary Tree
// (https://leetcode.com/problems/minimum-depth-of-binary-tree/#/description)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

import "math"

func minDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    if root.Left == nil && root.Right == nil {
        return 1
    }
	leftDepth, rightDepth := math.MaxInt32, math.MaxInt32
	if root.Left != nil {
		leftDepth = minDepth(root.Left)
	}
	if root.Right != nil {
		rightDepth = minDepth(root.Right)
	}
	if leftDepth < rightDepth {
		return leftDepth + 1
	}
	return rightDepth + 1
}
