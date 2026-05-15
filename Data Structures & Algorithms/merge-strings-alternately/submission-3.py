class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        ans = []
        for i in range(max(m, n)):
            if i < m:
                ans.append(word1[i])
            if i < n:
                ans.append(word2[i])
        return "".join(ans)