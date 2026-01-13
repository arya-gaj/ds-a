class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def diff(y):
            below = above = 0.0
            for _, y0, l in squares:
                top = y0 + l
                if y <= y0:
                    above += l * l
                elif y >= top:
                    below += l * l
                else:
                    below += (y - y0) * l
                    above += (top - y) * l
            return below - above

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):
            mid = (low + high) / 2
            if diff(mid) < 0:
                low = mid
            else:
                high = mid

        return low        