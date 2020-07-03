package homework

/**
 *@File:binary-tree-preorder-traversal
 * @Author: jokky
 * @Date: 2020/7/3 5:30 下午
 * @Desc:
 */

// Tree Preorder Traversal

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func preorderTraversal(root *TreeNode)[]int  {
	return preorderRecursive(root)
}

func preorderRecursive(root *TreeNode) []int {
	if root == nil{
		return []int{}
	}
	rest := append([]int{root.Val}, preorderRecursive(root.Left)...)
	rest = append(rest, preorderRecursive(root.Right)...)
	return rest
}

