#trial 4
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        one = nums[0]
        two = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp=two
            two=max(two,one+nums[i])
            one=temp
        return two


#trial 3
'''class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        res=[0]*len(nums)
        res[0]=nums[0]
        res[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            res[i]=max(res[i-1], nums[i]+res[i-2])
        return res[-1]'''



#trial 2
'''class Solution:
    def rob(self, nums: List[int]) -> int:
        res=[-1]*len(nums)
        def dfs(i):
            if i<len(nums) and res[i]!=-1:
                return res[i]
            if i >= len(nums):
                return 0
            #if res[i]!=-1:
            #    return res[i]
            res[i]=max(dfs(i + 1),nums[i] + dfs(i + 2))
            return res[i]
        
        return dfs(0)'''

#trial 1
'''class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==2:
            return max(nums[0],nums[1])
        elif len(nums)==1:
            return nums[0]

        return max(self.rob(nums[1:]),nums[0]+self.rob(nums[2:]))'''