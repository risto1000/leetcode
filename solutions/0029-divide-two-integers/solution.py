class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        is_negative = (dividend < 0) != (divisor < 0)
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)


        while abs_dividend>=abs_divisor:
            multiple = abs_divisor
            count_for_multiple = 1
            while multiple + multiple < abs_dividend:
                multiple <<= 1
                count_for_multiple <<= 1
            abs_dividend = abs_dividend - multiple
            count += count_for_multiple

        if is_negative:
            count = int(str("-")+str(count))

        if count > 2**31-1:
            count = 2**31-1
        if count < -2**31:
            count = -2**31
        return count
        
