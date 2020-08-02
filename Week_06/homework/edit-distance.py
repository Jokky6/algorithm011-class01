# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        inf = float('inf')
        dp = [[inf] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        dp[0][0] = 0
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        def helper(i, j):
            if dp[i][j] != inf or i * j == 0:
                return dp[i][j]
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = helper(i - 1, j - 1)
            else:
                dp[i][j] = 1 + min(helper(i - 1, j - 1), helper(i - 1, j), helper(i, j - 1))

            return dp[i][j]

        helper(len(word1), len(word2))
        return dp[len(word1)][len(word2)]