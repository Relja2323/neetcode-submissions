class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []


        desno = 1

        for i in range(len(nums)):
            if i == 0:
                res.append(1)
            else:
                res.append(nums[i-1]*res[i-1])
        for i in range(len(nums)-2, -1, -1):
            desno = desno * nums[i+1]
            res[i] = desno * res[i]
        
        return res
