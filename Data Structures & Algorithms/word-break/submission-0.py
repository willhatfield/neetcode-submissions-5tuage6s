class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        res = [False] * (n + 1)
        res[0] = True

        for i in range(n):
            if res[i]:
                for word in wordDict:
                    lenWord = len(word)

                    if i + lenWord <= n:
                        curr = s[i:(i+lenWord)]
                        if curr == word:
                            res[i + lenWord] = True

        
        return res[n]