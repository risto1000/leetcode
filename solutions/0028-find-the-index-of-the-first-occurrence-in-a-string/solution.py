class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        d = -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i

        return d
