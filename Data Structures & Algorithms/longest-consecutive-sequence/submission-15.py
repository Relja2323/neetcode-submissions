class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        left = 0
        right = 1
        maxLength = 1
        trenLength = 0

        nums.sort()

        if len(nums) == 0:
            return 0

        while right < len(nums):
            if nums[right] == nums[left]:
                left += 1
                right += 1
            elif nums[right] - nums[left] == 1:
                trenLength += 1
                left += 1
                right += 1
                if trenLength > maxLength:
                    maxLength = trenLength
            else:
                trenLength += 1
                if trenLength > maxLength:
                    maxLength = trenLength
                trenLength = 0
                left +=1
                right+=1
        if nums[len(nums)-1] - nums[len(nums)-2] == 1 or nums[len(nums)-1] - nums[len(nums)-2] == 0:
            trenLength +=1
        if trenLength > maxLength:
            maxLength = trenLength
        return maxLength

