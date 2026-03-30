class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num) - 1] < 0:
                return abs(num)
            else:
                nums[abs(num) - 1] *= -1
            

        return abs(nums[-1])