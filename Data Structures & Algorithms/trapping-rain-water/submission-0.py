class Solution:
    def trap(self, height: List[int]) -> int:
        if(len(height) <= 2):
            return 0

        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        puddle = 0

        while(l <= r):
            if lmax <= rmax:
                if height[l] < lmax:
                    puddle += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if height[r] < rmax:
                    puddle += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1

        return puddle