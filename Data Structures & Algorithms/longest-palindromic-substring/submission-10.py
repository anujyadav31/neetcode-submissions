#3. Two Pointers
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ri,rl=0,0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>rl:
                    ri=l
                    rl=r-l+1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>rl:
                    ri=l
                    rl=r-l+1
                l-=1
                r+=1
        return s[ri:ri+rl]

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
