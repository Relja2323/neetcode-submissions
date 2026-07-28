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
            maks = max(dict,key=dict.get)
            lista.append(maks)
            del dict[maks]

        return lista

