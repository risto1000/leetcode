class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestSum = math.inf
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:                    
                currentSum = nums[i]+nums[j]+nums[k]
                if abs(currentSum - target) < abs(closestSum - target): 
                    closestSum = currentSum
                if currentSum < target:
                    j+=1
                elif currentSum > target:
                    k-=1
                elif currentSum == target:
                    return currentSum
        return closestSum
