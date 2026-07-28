class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for x in nums:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] +=1
        lista =[]

        for i in range(k):
            lista.append(max(dict,key=dict.get))
            del dict[max(dict,key=dict.get)]

        return lista

