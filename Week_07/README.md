# 学习笔记 极客大学 11期1班

## 算法训练营 第七周学习总结
### 字典树和并查集  
    字典树
        即 Trie 树，又称单词 查找树或键树，是一种树形结 构。典型应用是用于统计和排 序大量的字符串（但不仅限于 字符串），所以经常被搜索引 擎系统用于文本词频统计。
        它的优点是：最大限度地减少 无谓的字符串比较，查询效率 比哈希表高。
        基本性质：1. 结点本身不存完整单词；
                 2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的 字符串；
                 3. 每个结点的所有子结点路径代表的字符都不相同。
        核心思想：Trie 树的核心思想是空间换时间。
                 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。
    
    并查集 
        基本操作：
            makeSet(s)：建立一个新的并查集，其中包含 s 个单元素集合。
            unionSet(x, y)：把元素 x 和元素 y 所在的集合合并，要求 x 和 y 所在 的集合不相交，如果相交则不合并。
             ﬁnd(x)：找到元素 x 所在的集合的代表，该操作也可以用于判断两个元 素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。

### 高级搜索  
    初级搜索
        1. 朴素搜索
        2. 优化方式：不重复（ﬁbonacci）、剪枝（生成括号问题）
        3. 搜索方向： DFS: depth ﬁrst search 深度优先搜索 BFS: breadth ﬁrst search 广度优先搜索 
        双向搜索、启发式搜索
        DFS 代码 - 递归写法 
            visited = set()  
            def dfs(node, visited):
             if node in visited: # terminator
             # already visited
             return
             visited.add(node)
             # process current node here.
             ...
             for next_node in node.children():
                if not next_node in visited:
                    dfs(next_node, visited)
         BFS 代码
             def BFS(graph, start, end):
               queue = []
               queue.append([start])
               visited.add(start)
               while queue:
                node = queue.pop()
                 visited.add(node)
                process(node)
                 nodes = generate_related_nodes(node) 
                queue.push(nodes) 
    回溯法 
        回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当 它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚 至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。
        回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：
            找到一个可能存在的正确的答案
            在尝试了所有可能的分步方法后宣告该问题没有答案
            在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。
  
 ### 二叉搜索树、AVL 树
    二叉搜索树，也称二叉搜索树、有序二叉树（Ordered Binary Tree）、排 序二叉树（Sorted Binary Tree），是指一棵空树或者具有下列性质的二叉 树：
        1. 左子树上所有结点的值均小于它的根结点的值； 
        2. 右子树上所有结点的值均大于它的根结点的值； 
        3. 以此类推：左、右子树也分别为二叉查找树。（这就是重复性！）
        中序遍历：升序排列   
    AVL 树
        1. 发明者G. M. Adelson-Velsky和Evgenii Landis
        2. Balance Factor（平衡因子）： 是它的左子树的高度减去它的右子树的高度（有时相反）。 balance factor = {-1, 0, 1}
        3. 通过旋转操作来进行平衡（四种)
        AVL 总结:
            1. 平衡二叉搜索树
            2. 每个结点存balance factor = {-1, 0, 1}
            3. 四种旋转操作
            不足：结点需要存储额外信息、且调整次数频繁
    红黑树
        红黑树是一种近似平衡的二叉搜索树（BinarySearch Tree），它能够确保任何一 个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉 搜索树：
        • 每个结点要么是红色，要么是黑色
        • 根结点是黑色
        • 每个叶结点（NIL结点，空结点）是黑色的。
        • 不能有相邻接的两个红色结点
        • 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。
        关键性质:从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。
