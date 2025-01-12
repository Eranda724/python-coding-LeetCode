from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                heights[i][j] = [heights[i][j], float('inf')]
                if i == 0 and j == 0:
                    heights[i][j][1] = 0

        for _ in range(len(heights) * len(heights[0])):
            for i in range(len(heights)):
                for j in range(len(heights[0])):
                    if i > 0:
                        heights[i][j][1] = min(
                            heights[i][j][1],
                            max(
                                abs(heights[i][j][0] - heights[i-1][j][0]),
                                heights[i-1][j][1]
                            )
                        )
                    if j > 0:
                        heights[i][j][1] = min(
                            heights[i][j][1],
                            max(
                                abs(heights[i][j][0] - heights[i][j-1][0]),
                                heights[i][j-1][1]
                            )
                        )
                    if j < len(heights[0]) - 1:
                        heights[i][j][1] = min(
                            heights[i][j][1],
                            max(
                                abs(heights[i][j][0] - heights[i][j+1][0]),
                                heights[i][j+1][1]
                            )
                        )
                    if i < len(heights) - 1:
                        heights[i][j][1] = min(
                            heights[i][j][1],
                            max(
                                abs(heights[i][j][0] - heights[i+1][j][0]),
                                heights[i+1][j][1]
                            )
                        )

        return heights[len(heights) - 1][len(heights[0]) - 1][1]
