package homework

import "container/heap"

/**
 *@File:top-k-frequent-elements
 * @Author: jokky
 * @Date: 2020/7/3 6:28 下午
 * @Desc:
 */

//给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

func topKFrequent(nums []int, k int) []int {
	if k == 0 || len(nums) == 0 {
		return make([]int, 0)
	}
	m := make(map[int]int)
	for _, v := range nums {
		m[v] = m[v] + 1
	}
	nodes := make(NodeHeap, 0, len(m))
	for k, v := range m {
		nodes = append(nodes, &Node{
			val:   k,
			times: v,
		})
	}
	h := &nodes
	heap.Init(h)
	topK := min(k, len(m))
	res := make([]int, 0, topK)
	for i := 0; i < topK; i++ {
		res = append(res, heap.Pop(h).(*Node).val)
	}
	return res
}

type Node struct {
	val   int
	times int
}

type NodeHeap []*Node

func (h NodeHeap) Len() int { return len(h) }

func (h NodeHeap) Less(i, j int) bool { return h[i].times > h[j].times }

func (h NodeHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *NodeHeap) Push(x interface{}) {
	*h = append(*h, x.(*Node))
}

func (h *NodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}