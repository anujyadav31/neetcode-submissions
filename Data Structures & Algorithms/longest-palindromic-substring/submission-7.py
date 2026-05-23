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
        return res

'''#Trial 1, Time O(2^n * n), Space O(n)
# Test case abaaa
# I solved for longest palindromic subsequence
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
