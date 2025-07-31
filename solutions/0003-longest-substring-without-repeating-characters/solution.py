class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sl = 0
        start = 0
        char_map = {}
        for i in range(len(s)):
            current_char = s[i]
            if current_char in char_map and char_map[current_char]>=start:
                start = char_map[current_char] + 1
            
            
            
            char_map[current_char] = i
            current_length = i - start + 1
            sl = max(sl, current_length)
            


        return sl
