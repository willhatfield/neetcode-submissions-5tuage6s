class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s

        res = ""

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                curr = s[i:j]
                if self.isPalindrome(curr) and len(curr) > len(res):
                    res = curr




        return res

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True