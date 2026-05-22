class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0

        for num in nums:
            if num == 1:
                count +=1 #counting

                # checking if count > maxCount
                if count > maxCount:
                    maxCount = count
            else:
                 # if num = 0 and count > 0 and count > maxCount
                if count > 0:
                    if count > maxCount:
                        maxCount = count
                    count = 0
        return maxCount
        

        