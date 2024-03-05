class Solution:
    def toLowerCase(self, s: str) -> str:
        res = list(s)
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90: res[i] = res[i].lower()
        return "".join(res)
