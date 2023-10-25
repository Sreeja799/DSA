class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        minIndex = float('inf')
        l = []

        for i in range(len(list1)):
            d[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in d:
                tempIndex = d[list2[i]] + i
                if tempIndex < minIndex:
                    minIndex = tempIndex
                    l = [list2[i]]
                elif tempIndex == minIndex:
                    l.append(list2[i])
        return l