class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l = []
        for rect in rectangles:
            l.append(min(rect))
        
        m = max(l)
        return l.count(m)       