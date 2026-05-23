class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2 or n==3:
            return n
        return Solution.climbStairs(self,n-1) + Solution.climbStairs(self,n-2)
        