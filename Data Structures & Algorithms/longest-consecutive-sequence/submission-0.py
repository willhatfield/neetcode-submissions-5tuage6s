class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            currNum = num
            currCount = 0
            while currNum in seen:
                currCount = currCount + 1
                currNum = currNum + 1
            longest = max(longest, currCount)

        return longest

        