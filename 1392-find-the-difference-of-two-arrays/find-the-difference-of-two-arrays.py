class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        temp1 = []
        temp2 = []

        d1 = {}
        d2 = {}
        for i in nums1:
            d1[i] = d1.get(i, 0) + 1
        for i in nums2:
            d2[i] = d2.get(i, 0) + 1
        
        for i in d1:
            if i not in d2:
                temp1.append(i)

        for i in d2:
            if i not in d1:
                temp2.append(i)

        return [temp1, temp2]