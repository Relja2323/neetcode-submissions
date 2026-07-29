class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for x in nums:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] +=1

        for num, count in dict.items():
            freq[count].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res





