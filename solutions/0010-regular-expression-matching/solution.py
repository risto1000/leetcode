class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1,n+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                s_char=s[i-1]
                p_char=p[j-1]
                if p_char == '.' or p_char == s_char:
                    dp[i][j]=dp[i-1][j-1]
                elif p_char =='*':
                    p_prev_char=p[j-2]
                    zo=dp[i][j-2]
                    oom=False
                    if p_prev_char=='.' or p_prev_char == s_char:
                        oom = dp[i-1][j]
                    dp[i][j]=zo or oom
                    
                else:
                    dp[i][j]=False
        return dp[m][n]

