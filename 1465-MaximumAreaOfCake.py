class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        MOD = 1000000007

        horizontalCuts += [0, h]
        verticalCuts += [0, w]

        horizontalCuts.sort()
        verticalCuts.sort()

        max_width = 0
        for i in range(1, len(horizontalCuts)):
            max_width = max(horizontalCuts[i] - horizontalCuts[i - 1], max_width)

        max_height = 0
        for i in range(1, len(verticalCuts)):
            max_height = max(verticalCuts[i] - verticalCuts[i - 1], max_height)

        return (max_width % MOD) * (max_height % MOD) % MOD