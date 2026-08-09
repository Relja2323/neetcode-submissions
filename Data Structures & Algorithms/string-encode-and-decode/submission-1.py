class Solution:

    def encode(self, strs: List[str]) -> str:

        for i in range(len(strs)):
            length = len(strs[i])
            strs[i] = str(length) + "#" + strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:

        stringovi = []
        broj = []
        trRec = []
        i = 0



        while i < len(s):
            while s[i] != "#":
                broj.append(s[i])
                i += 1
            i += 1
            for _ in range(int("".join(broj))):
                trRec.append(s[i])
                i +=1
            stringovi.append("".join(trRec))
            broj.clear()
            trRec.clear()


        return stringovi

