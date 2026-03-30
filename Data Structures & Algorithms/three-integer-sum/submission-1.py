class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            complement = 0 - num
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == complement:
                    ans = [num, nums[l], nums[r]]
                    if ans not in res:
                        res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                else:
                    if nums[l] + nums[r] > complement:
                        r -= 1
                    else:
                        l += 1
        
        return res