class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n < 2:
            return n
        
        l, r = 0, 0

        substring = set()
        res = 1
        while r < n:
            if s[r] not in substring:
                res = max(res, r - l + 1)
                substring.add(s[r])
            else:
                while l <= r:
                    if s[l] == s[r]:
                        l += 1
                        break
                    else:
                        substring.remove(s[l])
                        l += 1
            r += 1
        
        return res
