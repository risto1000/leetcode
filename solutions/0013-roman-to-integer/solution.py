class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        n = len(s)
        total = roman_map[s[n-1]]
        for i in range(n-2,-1,-1):
            current_val = roman_map[s[i]]
            next_val = roman_map[s[i+1]]

            if current_val < next_val:
                total -= current_val
            else:
                total += current_val
        return total 
