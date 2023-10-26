class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 100
        for i in s:
            if width >= widths[ord(i) - ord('a')]:
                width -= widths[ord(i) - ord('a')]
            else:
                width = 100 - widths[ord(i) - ord('a')]
                lines += 1
        return [lines, 100-width]      