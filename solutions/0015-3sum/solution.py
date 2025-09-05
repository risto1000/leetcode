class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            l,k = i+1, len(nums) - 1
            while l < k:
                threeSum = a + nums[l] + nums[k]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[l], nums[k]])
                    l += 1
                    k -= 1
                    while l < k and nums[l] == nums[l-1]:
                        l += 1
                    while l < k and nums[k] == nums[k+1]:
                        k -= 1
                    
        return res
