class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        arr = [folder[0]]

        for i in range(1, len(folder)):
            if not folder[i].startswith(arr[-1] + '/'):
                arr.append(folder[i])

        return arr
