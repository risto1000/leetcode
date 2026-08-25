class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def etsiRaja(nums, target, isFirst):
            left = 0
            right = len(nums) - 1 
            ans = -1
            while left <= right:
                mid = (right + left) //2 
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    ans = mid 
                    if isFirst == True:
                        right = mid - 1
                        
                    else :
                        left = mid + 1
            return ans
                    



        first = etsiRaja(nums, target, True)
            
        last = etsiRaja(nums, target, False)
        return [first, last]     

