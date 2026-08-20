class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use pivot sort
        # if nums[mid] > nums[l], search l to mid - 1. This isnt full proof, actually
        # as consider [2, 3, 1]
        # so if nums[r] < nums[mid], l = mid + 1
        # if nums[mid] < nums[l], update l = mid and search from l to r

        # [3,4,5,6,1,2]
        #  l.    m   r.      nums[r] < nums[mid] -> l = m + 1
        # [3,4,5,6,1,2]
        #         l/m;r.     nums[m] < nums[r], r = m, break, found minimum

        # [1,2,3,4,5,6]      
        #  l     m   r       nums[r] > nums[m], r = m
        # 
        
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
