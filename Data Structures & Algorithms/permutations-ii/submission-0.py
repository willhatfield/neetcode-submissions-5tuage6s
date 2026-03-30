class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            newPerms = []
            seen = set()
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, num)
                    pTuple = tuple(pCopy)
                    if pTuple not in seen:
                        seen.add(pTuple)
                        newPerms.append(pCopy)
            perms = newPerms
            
        return perms