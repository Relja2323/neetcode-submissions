class Solution:

    def encode(self, strs: List[str]) -> str:

        for i in range(len(strs)):
            length = len(strs[i])
            strs[i] = str(length) + "#" + strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:

        stringovi = []
        
        i = 0



        while i < len(s):
            broj = []
            trRec = []
            while s[i] != "#":
                broj.append(s[i])
                i += 1
            i += 1
            length = int("".join(broj))
            for _ in range(length):
                trRec.append(s[i])
                i +=1
            stringovi.append("".join(trRec))
 


        return stringovi

