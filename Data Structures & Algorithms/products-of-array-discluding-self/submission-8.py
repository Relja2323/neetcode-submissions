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

        levo, desno = [], [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                levo.append(1)
            else:
                levo.append(nums[i-1]*levo[i-1])
        for i in range(len(nums)-1, -1, -1):
            if i == (len(nums)-1):
                desno[i] = 1
            else:
                desno[i] = nums[i+1]*desno[i+1]


               
        
        if flag == 0:
            for i in range(len(nums)):
                res.append(desno[i]*levo[i])            
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
