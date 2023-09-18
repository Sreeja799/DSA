class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftindex = -1
        rightindex = -1

        def binarySearch(nums, target, flag):
            index = -1
            l = 0
            r = len(nums) - 1
            while (l <= r):
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    index = mid
                    if flag == -1:
                        r = mid - 1
                    else:
                        l = mid + 1
            return index
            
        left = binarySearch(nums, target, -1)
        right = binarySearch(nums, target, 1)
        return left, right