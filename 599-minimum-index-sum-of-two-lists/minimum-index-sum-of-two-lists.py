class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indexSum = float('inf')
        common = []
        for i in range(len(list1)):
            if list1[i] in list2:
                tempSum = i + list2.index(list1[i])
                if tempSum == indexSum:
                    common.append(list1[i])
                elif tempSum < indexSum:
                    common = [list1[i]]
                    indexSum = tempSum
        return common        