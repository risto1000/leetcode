class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer1=0
        pointer2=1
        sum=None
        while sum!=target:
            if pointer1==pointer2:
                pointer2+=1
            sum=nums[pointer1]+nums[pointer2]
            if sum!=target and pointer2 != len(nums)-1:
                pointer2 += 1
            elif sum != target:
              #  if sum != target:
                pointer2 = 0
                pointer1 +=1

        return [pointer1,pointer2]
