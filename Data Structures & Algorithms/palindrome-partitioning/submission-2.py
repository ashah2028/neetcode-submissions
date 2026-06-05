class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =[]
        partition = []

        def dfs(index):
            if index >= len(s):
                res.append(partition.copy())
                return
            for j in range(index, len(s)):
                if self.isPali(s, index, j):
                    partition.append(s[index : j + 1])
                    dfs(j + 1)
                    partition.pop()
        
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
