class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lis = {}
        for word in strs:
            sorted_word =''.join(sorted(word))
            if sorted_word not in lis:
                lis[sorted_word] = [word]
            else:
                lis[sorted_word].append(word)

        lista = list(lis.values())
        
        return lista