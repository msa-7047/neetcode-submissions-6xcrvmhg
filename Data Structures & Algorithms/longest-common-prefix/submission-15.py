class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            prefix += strs[0][i]
            for j in strs:
                if prefix != j[:i + 1]:
                    return prefix[:i]
        return prefix