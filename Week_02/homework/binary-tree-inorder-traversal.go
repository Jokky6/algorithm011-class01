package homework

/**
 *@File:binary-tree-inorder-traversal
 * @Author: jokky
 * @Date: 2020/7/3 6:19 下午
 * @Desc:
 */

// Tree Inorder Traversal

//type TreeNode struct {
//	Val int
//	Left *TreeNode
//	Right *TreeNode
//}

func inorderTraversal(root *TreeNode)[]int  {
	return inorderRecursive(root)
}

func inorderRecursive(root *TreeNode)[]int  {
	if root == nil{
		return []int{}
	}
	rest := append(inorderRecursive(root.Left), root.Val)
	rest = append(rest, inorderRecursive(root.Right)...)
	return rest
}