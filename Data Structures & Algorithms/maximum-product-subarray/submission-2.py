class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        curr_max, curr_min = nums[0], nums[0]
        res = nums[0]

        for i in range(1, n):
            num = nums[i]
            temp_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, curr_max * num, curr_min * num)
            curr_max = temp_max
            res = max(curr_max, res)

        return res
                



            
        