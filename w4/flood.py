class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        p = image[sr][sc]
        if p == color:
            return image

        def dfs(i, j):
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == p:
                image[i][j] = color
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        dfs(sr, sc)
        return image