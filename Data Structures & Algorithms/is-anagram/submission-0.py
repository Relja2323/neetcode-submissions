class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        first = {}
        second = {}

        for x in s:
            if x not in first:
                first[x] = 1
            else:
                first[x] += 1

        for y in t:
            if y not in second:
                second[y] = 1
            else:
                second[y] += 1

        return first == second