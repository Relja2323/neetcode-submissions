class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        brojevi = set(nums)
        maxLength = 0

        for num in brojevi:
            if num - 1 not in brojevi:
                i = 1
                currLength = 1
                while num + i in brojevi:
                    currLength += 1
                    i += 1
                maxLength = max(currLength, maxLength)
        
        return maxLength