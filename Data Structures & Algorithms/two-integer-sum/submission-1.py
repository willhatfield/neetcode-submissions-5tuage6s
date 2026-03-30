class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                comp = seen[complement]
                return [comp, i]
            else:
                seen[nums[i]] = i