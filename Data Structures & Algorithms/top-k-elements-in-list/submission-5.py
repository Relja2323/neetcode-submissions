class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] +=1
        lista =[]

        for i in range(k):
            maks = max(count,key=count.get)
            lista.append(maks)
            del count[maks]

        return lista

