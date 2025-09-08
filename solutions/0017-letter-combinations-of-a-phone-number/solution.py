class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        if digits == "":
            return []

        c_c = []
        result = []
        def backtrack(index):
            if index == len(digits):
                result.append("".join(c_c))
                return
            digit = digits[index]
            letters = phone_map[digit]
            for letter in letters: 
                c_c.append(letter)
                backtrack(index+1)
                c_c.pop()
        backtrack(0)
        return result

        
