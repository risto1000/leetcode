class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX= 2**31-1
        INT_MIN=-2**31

        i=0
        n=len(s)

        while i < n and s[i]==' ':
            i+=1
        sign=1
        if i < n:
            if s[i] and s[i]=='+':
                i+=1
            elif s[i] and s[i]=='-':
                i+=1
                sign=-1
        ret=0
        while i < n and s[i].isdigit():
            digit=int(s[i])
            if ret > INT_MAX // 10 or (ret==INT_MAX//10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            ret=10*ret+digit
            i+=1

        return sign*ret

