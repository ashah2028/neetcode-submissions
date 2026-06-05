class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        res = []
        comb = []

        def backtrack(i):
            if len(comb) == len(digits):
                res.append("".join(comb))
                return
            for c in dic[digits[i]]:
                comb.append(c)
                backtrack(i + 1)
                comb.pop()
        if digits:
            backtrack(0)
        return res

        