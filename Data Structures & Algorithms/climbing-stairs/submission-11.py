class Solution:
    def __init__(self):
        self.a=[1,2,3]
    def climbStairs(self, n: int) -> int:

        if n<=3:
            return n
        for i in range(4,n+1):
            self.a.append(self.a[i-2]+self.a[i-3])
        return self.a[n-1]
        