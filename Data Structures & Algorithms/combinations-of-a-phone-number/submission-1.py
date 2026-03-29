class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = "", "","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"
        path = []
        ans = []
        def dfs(i):
            if i == len(digits):
                ans.append(''.join(path))
                return
            for c in mapping[int(digits[i])]:
                path.append(c)
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans