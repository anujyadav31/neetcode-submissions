class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            tperm = []
            for p in perms:
                for i in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(i, num)
                    tperm.append(pcopy)
            perms = tperm
        return perms



        