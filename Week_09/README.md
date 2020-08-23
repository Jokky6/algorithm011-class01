## 学习笔记
### 字符串匹配算法
    暴力法
        public static int forceSearch(String txt, String pat) {
            int M = txt.length();
            int N = pat.length();
            for (int i = 0; i <= M - N; i++) {
        		int j;
                for (j = 0; j < N; j++) {
        			if (txt.charAt(i + j) != pat.charAt(j))
        				break;
        		}
                if (j == N) {
        			return i;
        		}
                // 更加聪明？
        		// 1. 预先判断– hash(txt.substring(i, M)) == hash(pat)
                // 2. KMP
        	}
            return -1;
        }
        
    Rabin-Karp 算法
        在朴素算法中，我们需要挨个比较所有字符，才知道目标字符串中是否包含 子串。那么， 是否有别的方法可以用来判断目标字符串是否包含子串呢？
        答案是肯定的，确实存在一种更快的方法。为了避免挨个字符对目标字符串 和子串进行比较， 我们可以尝试一次性判断两者是否相等。因此，我们
        需 要一个好的哈希函数（hash function）。 通过哈希函数，我们可以算出子 串的哈希值，然后将它和目标字符串中的子串的哈希值进行比较。
        这个新 方法在速度上比暴力法有显著提升。
        Rabin-Karp 算法的思想：
            1. 假设子串的长度为 M (pat)，目标字符串的长度为 N (txt)
            2. 计算子串的 hash 值 hash_pat
            3. 计算目标字符串txt中每个长度为 M 的子串的 hash 值（共需要计算 N-M+1 次）
            4. 比较 hash 值：如果 hash 值不同，字符串必然不匹配; 如果 hash 值相同， 还需要使用朴素算法再次判断
            
    KMP 算法
        KMP算法（Knuth-Morris-Pratt）的思想就是，当子串与目标字符串不匹配时， 其实你已经知道了前面已经匹配成功那 一部分的字符（包括
        子串与目标字符 串）。以阮一峰的文章为例，当空格与 D 不匹配时，你其实 知道前面六个字符是 “ABCDAB”。KMP 算法的想法是，设法利用
        这个已知信息，不要把“搜索位 置” 移回已经比较过的位置，继续把它向后移，这样就提高了效率。 
        

###  63.不同路径 2 这道题目的状态转移方程。
    状态转移方程: 
    dp[i][j] = dp[i−1,j] + dp[i,j−1]; (i,j)上无障碍物
    dp[i][j] = 0; (i,j)上有障碍物
    
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int[] dp = new int[n];
        dp[0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) dp[j] = 0;
                else if (j - 1 >= 0) dp[j] += dp[j-1];
            }
        }
        return dp[n-1];
    }