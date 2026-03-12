class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for word in dictionary:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    dp[i] = min(dp[i], dp[i + len(word)])
        return dp[0]