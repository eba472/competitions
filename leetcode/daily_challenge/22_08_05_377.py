class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = [0] * (target + 1)
        
        res[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    res[i] += res[i - num]
        return res[-1]