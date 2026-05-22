class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        curr_max = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr_max += 1
                best = max(best, curr_max)
            elif nums[i] == 0:
                curr_max = 0
        if best > curr_max:
            return best
        return curr_max
        

        