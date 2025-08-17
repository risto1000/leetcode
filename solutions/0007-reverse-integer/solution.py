class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX=2**31-1
        INT_MIN=-2**31

        
        sign= 1 if x >= 0 else -1
        x=abs(x)
        r_s=str(x)[::-1]
        r_i=int(r_s)
        ret=sign*r_i
        if ret < INT_MIN or ret > INT_MAX:
            return 0
        return ret

