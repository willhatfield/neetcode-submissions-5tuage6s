class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if(nums[0] >= target):
            return 1
        l, r = 0, 1
        currMin = 0
        currSum = nums[l] + nums[r]

        while(l <= r and r < len(nums)):
            if currSum < target:
                r = r + 1
                if r >= len(nums):
                    return currMin
                else:
                    currSum = currSum + nums[r]
            else:
                if currMin == 0:
                    currMin = r - l + 1
                else:
                    currMin = min(currMin, r - l + 1)
                    if currMin == 1:
                        return 1
                    else:
                        currSum = currSum - nums[l]
                        l = l + 1
                        
        return currMin
        