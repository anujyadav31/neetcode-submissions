# abbc
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            l, r = 0, 0
            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 
                       and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p
        
        p = manacher(s)
        resLen, center_idx = max((v, i) for i, v in enumerate(p))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx : resIdx + resLen]

'''#2. Dynamic Programming
# ababa
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]'''       

'''
#1. Brute Force
# abcaacba
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res,rl='',0
        for i in range(len(s)):
            for j in range (i,len(s)):
                l,r=i,j
                while l<r and s[l]==s[r]:
                    l=l+1
                    r=r-1
                if l>=r and rl<(j-i+1):
                    res=s[i:j+1]
                    rl=j-i+1
        return res'''

'''#I solved for longest palindromic subsequence
#Trial 1, Time O(2^n * n), Space O(n)
# abaaa
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        t=[]
        res=[]
        ln=0
        r=''

        def palin(temp1):
            nonlocal ln
            nonlocal res
            nonlocal r
            j=int(len(temp1)/2)

            for i in range(j):
                if temp1[i]!=temp1[-1-i]:
                    return 
            if len(temp1)>ln:
                ln=len(temp1)
                res=temp1
                r=''.join(res)

            return r

        def dfs(i):
            nonlocal l
            nonlocal t
            if i==l:
                palin(t)
                return 
            t.append(s[i])
            dfs(i+1)
            t.pop()
            dfs(i+1)

        dfs(0)
        return r'''
