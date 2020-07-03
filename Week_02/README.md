# 学习笔记 极客大学 11期1班
## 算法训练营 第二周学习总结 —— Golang

### 树(Tree)

二叉树的遍历:

前序(Pre-order): 根-左-右
中序(In-order): 左-根-右
后序(Post-order): 左-右-根

巧记：根节点相对于其他节点的位置

二叉搜索树:也称为有序二叉树、排序二叉树，是指一颗空树或者具有下列性质的二叉树

1、左子树上的`所有节点`的值均小于它的根节点的值
2、右子树上的`所有节点`的值均大于它的根节点的值
3、以此类推：左、右子树也分别为二叉搜索树

特性:二叉搜索树中序遍历的内容是一个从小到大排序的数组

### 堆(Heap)

堆(Heap)是一种特殊的树状数据结构。
若是满足以下特性，即可称为堆:
给定堆中任意节点 P 和 C，若 P 是 C 的母节点，那么 P 的值会小于等于（或大于等于） C 的值

作用:能在logN复杂度下获取一组可以动态扩容数据流的最小(最大)值,用于实现优先级队列。

### 图(Graph)

在计算机科学中,一个图就是一些顶点的集合,这些顶点通过一系列边结对(连接),顶点用圆圈表示,边就是这些圆圈之间的连线,顶点之间通过边连接。

DFS:
```python
visited=set()
def dfs(node,visited):
  visited.add(node)
  #process currect node here
  process(node)
  for next_node in node.children:
    if not next_node in visited:
      dfs(next_node,visited)
```

BFS:
```python
def BFS(graph,start,visited):
    queen=[]
    queen.append(start)
    while queen:
        node=queen.pop()
        visited.add(node)
        process(node)
        for next_node in node.children:
            if next_node not in visited:
                queen.append(next_node)
```