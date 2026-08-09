class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        proizvod = 1
        flag = 0
        for num in nums:
            if num != 0:
                proizvod *= num
            else:
                flag += 1
        
        if flag == 0:
            for i in range(len(nums)):
                res.append(proizvod//nums[i])    
        elif flag == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(proizvod)
        elif flag > 1:
            for i in range(len(nums)):
                res.append(0)
        return res
