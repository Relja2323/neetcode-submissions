class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        brojevi = {}

        for i in range(len(nums)):
            if target - nums[i] in brojevi:
                return[brojevi[target - nums[i]],i]
            else:
                brojevi[nums[i]] = i