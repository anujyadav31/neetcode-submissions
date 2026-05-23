class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            c=0
            for j in nums:
                if i==j:
                    c+=1
            if c>1:
                return True
        return False

         