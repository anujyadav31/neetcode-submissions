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

        return dfs(0)
        



'''class Solution:
    def numDecodings(self, s: str) -> int:
        a=[-1]*len(s)
        res=0
        c=[0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',0,0,0,0]
        def dec(i):
            if i>= len(s):
                return 1
            return dec(i)+dec(i+2)
            nonlocal a
            nonlocal c
            nonlocal res
            if len(b)==0:
                res+=1
                return ''
            if len(b)==1:
                return c[ord(b[0])-48]
            #if b[0]=='':
             #   return ''
            if len(b)>=2 and b[1]=='0':
                return c[(ord(b[0])-48)*10+(ord(b[1])-48)]+dec(b[2:])
                
            #stoi()
            if len(b)>=2:
                c[ord(b[0])-48]+dec(b[1:])
                if (ord(b[0])-48)*10+(ord(b[1])-48)<=26:
                    c[(ord(b[0])-48)*10+(ord(b[1])-48)]+dec(b[2:])
            return res
        dec(0)'''
        