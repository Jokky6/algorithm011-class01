# 学习笔记 极客大学 11期1班

## 算法训练营 第四周学习总结

### 深度优先搜索(DFS)

> 递归
```python
#递归前处理
visited = set()  # 节点是否被访问

def dfs(node,visited):
    # 递归终止条件
    if node in visited: # 是否被访问
        return
    
    # 递归到下一层前处理（当前层处理）
    visited.add(node) 
    # 其它处理

    # 递归到下一层

    for next_node in node.children(): 
        if not next_node in visited: 
            dfs(next_node, visited)

    # 递归下层次返回后处理

```
> 迭代实现 栈
```python
def dfs(node,visited):

    if tree.root is None: 
		return [] 
    # 迭代前处理
	visited, stack = [], [tree.root]    # 辅助栈 压栈
    # 迭代终止条件
    while stack: 
        # 迭代
        node = stack.pop()  # 出栈
        visited.add(node)   # 标记访问

        rocess (node)   # 当前节点处理

        nodes = generate_related_nodes(node)  # 生成相关节点
        stack.push(nodes) # 压栈
    # 迭代后处理
```

### 广度优先搜索(BFS)

> 迭代 队列
```python
def bfs(graph, start, end):
    # 迭代前处理
    queue = [] # 辅助队列
    queue.append([start])   # 入队列
    visited.add(node)   # 标记访问
    # 迭代终止条件
    while queue:
        # 迭代  
        node = queue.pop(0)  # 出队列
        visited.add(node)   # 标记访问

        rocess (node)   # 当前节点处理
        nodes = generate_related_nodes(node)  # 生成相关节点
        queue.push(nodes) # 入队列

    # 迭代后处理     
```

### 二分查找

```python

left, right = 0, len(array) - 1 
while left <= right: 
	  # mid = (left + right) / 2
      mid = low + (high-low)/2
	  if array[mid] == target: 
		    # 找到目标
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1

```

### 贪心算法 动态规划 区别

> 动态规划和贪心算法都是一种递推算法

> 贪心算法：
> 1.贪心算法中，作出的每步贪心决策都无法改变，因为贪心策略是由上一步的最优解推导下一步的最优解，而上一部之前的最优解则不作保留。
> 2.由（1）中的介绍，可以知道贪心法正确的条件是：每一步的最优解一定包含上一步的最优解。

> 动态规划算法：

> 1.全局最优解中一定包含某个局部最优解，但不一定包含前一个局部最优解，因此需要记录之前的所有最优解
> 2.动态规划的关键是状态转移方程，即如何由以求出的局部最优解来推导全局最优解
> 3.边界条件：即最简单的，可以直接得出的局部最优解
