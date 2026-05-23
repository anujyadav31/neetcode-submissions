class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        rob1 = rob2 = rob3 = rob4 = temp = 0
        for i in range(0,len(nums)-1):
            temp = rob2
            rob2 = max(rob2, rob1 + nums[i])
            rob1 = temp

        for i in range(1,len(nums)):
            temp = rob4
            rob4 = max(rob4, rob3 + nums[i])
            rob3 = temp

        return max(rob2, rob4)