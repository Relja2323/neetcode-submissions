class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        merged = list(zip(position,speed))
        merged.sort(reverse=True)

        stack = []

        for i in range(len(merged)):
            vreme = (target - merged[i][0]) / merged[i][1]
            if not stack or stack[-1] < (vreme):
                stack.append(vreme)

        return len(stack)        