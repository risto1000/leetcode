class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        



        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m,n=len(nums1),len(nums2)
        low, high = 0, m
        total_length = m+n

        while low <= high:
            partitionX = (low+high)//2
            partitionY = (total_length + 1) // 2 - partitionX
            maxLeftX = nums1[partitionX-1] if partitionX != 0 else -math.inf
            minRightX = nums1[partitionX] if partitionX != m else math.inf
            maxLeftY = nums2[partitionY-1] if partitionY != 0 else -math.inf
            minRightY = nums2[partitionY] if partitionY != n else math.inf


            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if total_length % 2 == 0:
                    max_of_left = max(maxLeftX, maxLeftY)
                    min_of_right = min(minRightX, minRightY)
                    return (max_of_left + min_of_right) / 2.0
                else:
                    return float(max(maxLeftX,maxLeftY))
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
            

