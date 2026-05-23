class Solution:
    def numDecodings(self, s: str) -> int:
        dp=dp2=0
        dp1=1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                dp=0
            else:
                dp=dp1
            if i+1<len(s) and (s[i]=='1' or s[i]=='2'and s[i+1]in '0123456'):
                dp+=dp2
            dp,dp1,dp2=0,dp,dp1

        return dp1
'''DP Top down
class Solution:
    def numDecodings(self, s: str) -> int:
        #dp = {len(s) : 1}
        dp={}

        def dfs(i):
            if i==len(s):
                dp[i]=1
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)'''
